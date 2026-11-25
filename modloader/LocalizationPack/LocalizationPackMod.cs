using System.IO;
using System.Linq;
using GamesByMalcs.Melvor2.Settings;
using Godot;
using MelvorModLoader;

namespace LocalizationPack;

/// <summary>
/// Melvor Mod Loader entry point. Does what the standalone override.cfg does: registers every language file
/// listed in mod.json and starts localization_pack.gd as the node "LocalizationPack".
/// </summary>
public class LocalizationPackMod : IMod
{
    const string NodeName = "LocalizationPack";   // same name as the autoload in override.cfg

    public void OnLoad(ModContext ctx)
    {
        // Installed with our own override.cfg as well: Godot has already loaded everything.
        if (ctx.Tree.Root.HasNode(NodeName))
        {
            ctx.Log("Already loaded through override.cfg, nothing to do.");
            return;
        }
        string dir = ctx.Directory.Replace('\\', '/');
        string configFile = Path.Combine(ctx.Directory, "mod.json");
        if (!File.Exists(configFile))
        {
            ctx.Log("mod.json not found in " + ctx.Directory);
            return;
        }
        var config = Json.ParseString(File.ReadAllText(configFile)).AsGodotDictionary();
        var languages = config["languages"].AsGodotDictionary();
        int gameLanguages = 0;
        var modLanguages = new System.Collections.Generic.SortedDictionary<string, int>();   // mod folder -> languages
        var englishNames = new System.Collections.Generic.Dictionary<string, string>();   // locale -> "Japanese"
        string modsDir = Path.Combine(ctx.Directory, "Languages", "Mods");
        string[] mods = Directory.Exists(modsDir) ? Directory.GetDirectories(modsDir) : [];
        foreach (var (key, value) in languages)
        {
            string code = key.AsString();
            var entry = value.AsGodotDictionary();
            englishNames[entry["locale"].AsString()] = entry["english_name"].AsString();
            string file = entry["file"].AsString();
            if (Load(dir + "/" + file, code))
                gameLanguages++;
            // The same language for other mods: Languages/Mods/<Mod>/<same file name>
            foreach (string mod in mods)
            {
                string modFile = Path.Combine(mod, Path.GetFileName(file));
                string name = Path.GetFileName(mod);
                if (File.Exists(modFile) && Load(modFile.Replace('\\', '/'), code))
                    modLanguages[name] = modLanguages.TryGetValue(name, out int count) ? count + 1 : 1;
            }
        }

        bool Load(string path, string code)
        {
            var translation = ResourceLoader.Load<Translation>(path);
            if (translation == null)
            {
                ctx.Log($"Could not load {path} ({code})");
                return false;
            }
            TranslationServer.AddTranslation(translation);
            return true;
        }
        // The game loads its settings before the loader runs, finds no catalog for the saved language and
        // replaces it with English in memory (the file still holds it). Put the saved value back through the
        // game's own setter, which also switches the language.
        void RestoreLanguage()
        {
            if (!LocalSettingsManager.SettingsLoaded || LocalSettingsManager.User == null)
                return;
            ctx.Frame -= RestoreLanguage;
            string? saved = ReadSavedLanguage();
            if (saved != null && englishNames.TryGetValue(saved, out string? name) && LocalSettingsManager.User.Language != saved)
            {
                LocalSettingsManager.User.Language = saved;
                ctx.Log($"Saved language restored: {name}");
            }
        }
        ctx.Frame += RestoreLanguage;
        var node = new Node { Name = NodeName };
        node.SetScript(GD.Load<GDScript>(dir + "/localization_pack.gd"));
        // Deferred: OnLoad runs during the first frame, while the scene tree is busy.
        ctx.Tree.Root.CallDeferred(Node.MethodName.AddChild, node);
        ctx.Log($"{gameLanguages} languages loaded for the game");
        if (modLanguages.Count > 0)
        {
            // "5 languages loaded for mods (ModLoader)", or per mod when the counts differ
            var counts = modLanguages.Values.Distinct().ToList();
            ctx.Log(counts.Count == 1
                ? $"{counts[0]} languages loaded for mods ({string.Join(", ", modLanguages.Keys)})"
                : $"Languages loaded for mods ({string.Join(", ", modLanguages.Select(m => $"{m.Key}: {m.Value}"))})");
        }
        ctx.Log("Runtime script started");
    }

    /// <summary>"Language" from the newest userSettings.json in the game's user folder, or null.</summary>
    static string? ReadSavedLanguage()
    {
        try
        {
            var file = new DirectoryInfo(OS.GetUserDataDir())
                .GetFiles("userSettings.json", SearchOption.AllDirectories)
                .OrderByDescending(f => f.LastWriteTimeUtc)
                .FirstOrDefault();
            if (file == null)
                return null;
            using var json = System.Text.Json.JsonDocument.Parse(File.ReadAllText(file.FullName));
            return json.RootElement.TryGetProperty("Language", out var value) ? value.GetString() : null;
        }
        catch (System.Exception)   // unreadable settings: keep the game's choice
        {
            return null;
        }
    }
}

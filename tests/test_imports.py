import importlib
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))


def test_imports_work_from_project_root():
    for module_name in ["Cyberpunk_2077", "Jogo", "Jogador", "Inimigo", "Loja", "Masmorra", "Arma", "Armadura", "Pocao", "Recursos", "Afterlife", "Companheiro"]:
        module = importlib.import_module(module_name)
        assert module is not None


def test_localizar_audio_works_when_cwd_changes(monkeypatch, tmp_path):
    from Recursos import Recursos

    monkeypatch.chdir(tmp_path)
    caminho = Recursos.localizarAudio("The-Rebel-Path-_Cyberpunk-2077-Soundtrack_.wav")

    assert caminho is not None
    assert Path(caminho).name == "The-Rebel-Path-_Cyberpunk-2077-Soundtrack_.wav"

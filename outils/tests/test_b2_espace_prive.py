"""Tests de cloisonnement de l'espace privé B2 (aucune publication)."""
import contextlib
import io
import json
import shutil
import tempfile
import unittest
from pathlib import Path

from b2_pipeline.cli import main


class EspacePriveTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        base = Path(self.temp.name)
        original = Path(__file__).resolve().parents[2]
        self.source = base / 'source'
        self.work = base / 'prive'
        course = 'qc-pri-ma-008'
        for rel in (f'cours/{course}.json',
                    f'kristals/{course}/authoring/CONTRAT_PEDAGOGIQUE.json'):
            target = self.source / rel
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(original / rel, target)

    def call(self, work, command='pilot'):
        with contextlib.redirect_stderr(io.StringIO()) as errors, \
             contextlib.redirect_stdout(io.StringIO()) as output:
            code = main(['--source', str(self.source), '--work', str(work), command])
        return code, output.getvalue(), errors.getvalue()

    def test_refuse_la_racine_source(self):
        code, _, error = self.call(self.source)
        self.assertEqual(code, 2)
        self.assertIn('Espace --work interdit', error)
        self.assertFalse((self.source / 'brouillons').exists())

    def test_refuse_un_sous_dossier_source(self):
        code, _, error = self.call(self.source / 'espace-prive')
        self.assertEqual(code, 2)
        self.assertIn('Espace --work interdit', error)
        self.assertFalse((self.source / 'espace-prive').exists())

    def test_refuse_le_lien_symbolique_vers_la_source(self):
        lien = self.source.parent / 'raccourci-vers-source'
        try:
            lien.symlink_to(self.source, target_is_directory=True)
        except (OSError, NotImplementedError):
            self.skipTest('Liens symboliques indisponibles')
        code, _, error = self.call(lien / 'brouillons')
        self.assertEqual(code, 2)
        self.assertIn('Espace --work interdit', error)

    def test_autorise_un_dossier_prive_externe(self):
        code, _, errors = self.call(self.work)
        self.assertEqual(code, 0, errors)
        draft = self.work / 'brouillons' / 'qc-pri-ma-008.json'
        self.assertTrue(draft.is_file())
        self.assertEqual(json.loads(draft.read_text(encoding='utf-8'))['editorial_status'], 'draft')
        self.assertFalse((self.source / 'brouillons').exists())


if __name__ == '__main__':
    unittest.main()

import unittest
from pathlib import Path

from utils.assets import image_data_uri, resume_available, resume_bytes
from utils.data import load_faq, load_profile, load_projects, load_skills, project_map
from utils.text import FALLBACK_ANSWER, answer_question, suggested_questions


class ContentTests(unittest.TestCase):
    def test_profile_has_required_sections(self):
        profile = load_profile()
        self.assertTrue(profile["name"])
        self.assertEqual(len(profile["education"]), 2)
        self.assertGreaterEqual(len(profile["experience"]), 3)
        self.assertEqual(len(profile["certifications"]), 8)
        self.assertEqual(profile["leadership"]["role"], "Secretary")
        self.assertNotIn("1,500+", str(profile))

    def test_projects_are_unique_and_complete(self):
        projects = load_projects()
        self.assertEqual(len(projects), 7)
        slugs = {project["slug"] for project in projects}
        repos = {project["repo_name"] for project in projects}
        self.assertEqual(len(slugs), 7)
        self.assertEqual(len(repos), 7)
        required = {
            "slug",
            "title",
            "summary",
            "highlights",
            "stack",
            "repo_name",
            "repo",
            "accent",
            "glyph",
        }
        for project in projects:
            self.assertTrue(required.issubset(project))
            self.assertTrue(project["highlights"])

    def test_skill_links_resolve_to_projects(self):
        projects = project_map()
        for skill in load_skills():
            self.assertTrue(skill["items"])
            for slug in skill["projects"]:
                self.assertIn(slug, projects)


class FaqTests(unittest.TestCase):
    def test_faq_ids_are_unique(self):
        entries = load_faq()
        ids = [entry["id"] for entry in entries]
        self.assertEqual(len(ids), len(set(ids)))
        self.assertTrue(all(entry["answer"] for entry in entries))

    def test_python_question_matches_python_entry(self):
        answer, entry_id = answer_question("Which projects use Python?", load_faq())
        self.assertEqual(entry_id, "python")
        self.assertIn("Python", answer)

    def test_unknown_question_uses_fallback(self):
        answer, entry_id = answer_question("What is the capital of France?", load_faq())
        self.assertEqual(answer, FALLBACK_ANSWER)
        self.assertIsNone(entry_id)

    def test_suggested_questions_are_ordered(self):
        suggestions = suggested_questions(load_faq(), limit=6)
        self.assertEqual(len(suggestions), 6)
        self.assertEqual(suggestions[0]["id"], "generative-ai")
        self.assertEqual(suggestions[1]["id"], "python")


class AssetTests(unittest.TestCase):
    def test_portrait_and_resume_exist(self):
        root = Path(__file__).resolve().parent.parent
        self.assertTrue((root / "assets" / "anu-profile.jpg").exists())
        self.assertTrue((root / "assets" / "favicon.png").exists())
        self.assertTrue(resume_available())
        self.assertTrue(resume_bytes().startswith(b"%PDF"))
        self.assertTrue(image_data_uri().startswith("data:image/jpeg;base64,"))


if __name__ == "__main__":
    unittest.main()

import pytest
from django.contrib.auth.models import User

from web_project.portal.models import Note, Tag


@pytest.mark.django_db
def test_note():
    user = User(username="test")
    user.save()

    note = Note(title="Note 1", content="This is a note content", author=user)
    note.save()

    tag = Tag(name="Tag 1")
    tag.save()
    note.tags.add(tag)

    assert list(note.tags.all()) == [tag]
    assert note.author == user

    # Remove user
    user.delete()

    note.refresh_from_db()
    assert note.author == User.objects.get(username="ghost")


@pytest.mark.django_db
def test_failing():
    user = User(username="test")
    user.save()

    note = Note(title="Note 2", content="This is another note content", author=user)
    note.save()

    assert note.author.username == "ghost"

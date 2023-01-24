import pytest
from fixture.application import Application
from model.contact import Contact


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.Destroy)
    return fixture


def test_add_contact(app):
    app.session.Login(email="denisprokofyev88@gmail.com", password="Probka98")
    app.contact.Add(Contact(FirstName='Denis', LastName='Prokofyev', Street='Petrozavodskaya'))
    app.session.Logout()

def test_add_contact_one_symbol(app):
    app.session.Login(email="denisprokofyev88@gmail.com", password="Probka98")
    app.contact.Add(Contact(FirstName='D', LastName='P', Street='P'))
    app.session.Logout()
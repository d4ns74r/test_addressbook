import pytest
from application import Application
from contact import Contact


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.Destroy)
    return fixture


def test_add_contact(app):
    app.Login(email="denisprokofyev88@gmail.com", password="Probka98")
    app.Add_new_contact(Contact(FirstName='Denis', LastName='Prokofyev', Street='Petrozavodskaya'))
    app.Logout()

def test_add_contact_one_symbol(app):
    app.Login(email="denisprokofyev88@gmail.com", password="Probka98")
    app.Add_new_contact(Contact(FirstName='D', LastName='P', Street='P'))
    app.Logout()
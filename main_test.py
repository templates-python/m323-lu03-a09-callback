import pytest
from main import GreetingApp

# Mock für das Hauptfenster von tkinter
@pytest.fixture
def mock_tk(mocker):
    try:
        mock = mocker.patch('tkinter.Tk', autospec=True, create=True)()
        mock.tk = mocker.MagicMock()  # Hinzufügen des 'tk'-Attributs
        mock.children = {}  # Hinzufügen des 'children'-Attributs
    except ModuleNotFoundError:
        mock = mocker.MagicMock()
        mock.tk = mocker.MagicMock()  # Hinzufügen des 'tk'-Attributs
        mock.children = {}  # Hinzufügen des 'children'-Attributs
    return mock

# Mock für den Button von tkinter
@pytest.fixture
def mock_button(mocker):
    return mocker.patch('tkinter.Button', autospec=True, create=True)()

@pytest.fixture
def mock_label(mocker):
    return mocker.patch('tkinter.Label', autospec=True, create=True)()

@pytest.fixture
def mock_entry(mocker):
    return mocker.patch('tkinter.Entry', autospec=True, create=True)()

def test_greet_user(mock_tk, mock_button, mock_label, mock_entry, mocker):
    app = GreetingApp(mock_tk)

    # Finden des richtigen Entry-Widgets und Mocken der get-Methode
    for attr in dir(app):
        widget = getattr(app, attr)
        if isinstance(widget, mocker.MagicMock) and widget._mock_name == 'Entry':
            mocker.patch.object(widget, 'get', return_value="Alice")
            break

    # Die greet_user-Methode aufrufen
    app.greet_user()

    # Überprüfen, ob das Label-Widget korrekt aktualisiert wurde
    for attr in dir(app):
        widget = getattr(app, attr)
        if isinstance(widget, mocker.MagicMock) and widget._mock_name == 'Label':
            widget.config.assert_called_with(text="Hallo, Alice!")
            break

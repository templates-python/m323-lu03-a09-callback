import tkinter as tk


class GreetingApp:
    """
    Eine einfache GUI-Anwendung, die es einem Benutzer ermöglicht, seinen Namen in ein Eingabefeld einzugeben.
    Nach Eingabe seines Namens und Klick auf einen Button wird eine Begrüßungsnachricht angezeigt.
    """

    def __init__(self, root):
        """
        Initialisiert die GUI-Komponenten.

        Args:
        - root (tk.Tk): Das Hauptfenster der Anwendung.
        """
        # TODO: Titel setzen und in root in self.root speichern

        # Label-Widget, das den Benutzer auffordert, seinen Namen einzugeben
        # TODO

        # Eingabefeld-Widget (Entry-Widget) für den Namen des Benutzers
        # TODO

        # Label-Widget für die Begrüßungsnachricht
        # Zu Beginn wird kein Text angezeigt
        # TODO

        # Button-Widget, das die greet_user-Methode aufruft, wenn es geklickt wird
        # TODO

    def greet_user(self):
        """
        Diese Methode wird aufgerufen, wenn der Benutzer auf den "Begrüßen"-Button klickt.
        Sie liest den Namen aus dem Eingabefeld aus und zeigt eine Begrüßungsnachricht unterhalb des Buttons an.
        """
        # Den eingegebenen Namen aus dem Entry-Widget holen
        # TODO
        # Begrüßungsnachricht generieren
        # TODO
        # Die Begrüßungsnachricht im Label-Widget anzeigen
        # TODO


if __name__ == '__main__':
    # Hauptfenster des GUI erstellen
    root = tk.Tk()

    # Instanz der GreetingApp-Klasse erstellen
    app = GreetingApp(root)

    # GUI-Event-Loop starten
    root.mainloop()

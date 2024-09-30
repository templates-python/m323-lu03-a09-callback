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
        self.root = root
        self.root.title("Begrüßungs-App")

        # Label-Widget, das den Benutzer auffordert, seinen Namen einzugeben
        self.label = tk.Label(root, text="Geben Sie Ihren Namen ein:")
        self.label.pack(pady=20)

        # Eingabefeld-Widget (Entry-Widget) für den Namen des Benutzers
        self.entry = tk.Entry(root)
        self.entry.pack(pady=20)

        # Label-Widget für die Begrüßungsnachricht
        # Zu Beginn wird kein Text angezeigt
        self.greeting_label = tk.Label(root, text="")
        self.greeting_label.pack(pady=20)

        # Button-Widget, das die greet_user-Methode aufruft, wenn es geklickt wird
        self.button = tk.Button(root, text="Begrüßen", command=self.greet_user)
        self.button.pack(pady=20)

    def greet_user(self):
        """
        Diese Methode wird aufgerufen, wenn der Benutzer auf den "Begrüßen"-Button klickt.
        Sie liest den Namen aus dem Eingabefeld aus und zeigt eine Begrüßungsnachricht unterhalb des Buttons an.
        """
        # Den eingegebenen Namen aus dem Entry-Widget holen
        name = self.entry.get()

        # Begrüßungsnachricht generieren
        greeting = f"Hallo, {name}!"

        # Die Begrüßungsnachricht im Label-Widget anzeigen
        self.greeting_label.config(text=greeting)


if __name__ == "__main__":
    # Hauptfenster des GUI erstellen
    root = tk.Tk()

    # Instanz der GreetingApp-Klasse erstellen
    app = GreetingApp(root)

    # GUI-Event-Loop starten
    root.mainloop()

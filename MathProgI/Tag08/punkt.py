class Punkt:

    # Initialisierung der Klasse
    def __init__(self, x, y):
        # Definiert x- und y-Wert
        self.X = x
        self.Y = y

        
    # Bezeichnung des Objektes
    def __str__(self):
        return "Punkt(%s,%s)"%(self.X, self.Y)
    

    # Methode zur Berechnung des Abstandes
    def Abstand(self, other):
        dx = self.X - other.X
        dy = self.Y - other.Y
        return (dx**2 + dy**2)**0.5

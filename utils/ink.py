class Stroke:
    """Represents a single handwriting stroke with x,y coordinates."""

    def __init__(self, list_of_coordinates=None):
        """Initialize a stroke from list of coordinate pairs.

        Args:
            list_of_coordinates (list, optional): List of (x,y) coordinate tuples
        """
        self.x = []
        self.y = []
        if list_of_coordinates:
            for point in list_of_coordinates:
                self.x.append(point[0])
                self.y.append(point[1])

    def __len__(self):
        return len(self.x)

    def __getitem__(self, index):
        return (self.x[index], self.y[index])


class Ink:
    """Container for multiple strokes comprising handwritten content."""

    def __init__(self, list_of_strokes=None):
        """Initialize ink object with list of strokes.

        Args:
            list_of_strokes (list, optional): List of Stroke objects
        """
        self.strokes = []
        if list_of_strokes:
            self.strokes = list_of_strokes

    def __len__(self):
        return len(self.strokes)

    def __getitem__(self, index):
        return self.strokes[index]

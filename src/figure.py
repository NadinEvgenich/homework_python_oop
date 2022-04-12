class Figure:
    area: int = None

    def add_area(self, figure):
        if isinstance(figure, Figure):
            return self.area + figure.area
        else:
            raise ValueError("Non-geometric figure passed!")

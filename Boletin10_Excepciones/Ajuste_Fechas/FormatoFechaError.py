class FormatoFechaError(Exception):
	def __init__(self, mensaje, dia, mes, anho):
		super().__init__()
		self.mensaje = mensaje
		self.dia = dia
		self.mes = mes
		self.anho = anho

	def __str__(self):
		fecha_str = f" ({self.dia}/{self.mes}/{self.ano})" if self.dia else ""
		return f"Error de Formato: {self.mensaje}{fecha_str}"

    ## Creacion de pull request
    ## Añadido por gael


	@staticmethod
	def validar(dia, mes, anho):
		if not (1970 <= int(anho) <= 2999):
			raise FormatoFechaError("El año esta fuera de rango (1970-2999", dia,mes,anho)
		if not (1 <= int(mes) <= 12):
			raise FormatoFechaError("El mes esta fuera de rango (1-12)", dia)
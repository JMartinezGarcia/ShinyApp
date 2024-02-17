from vetiver import VetiverAPI, VetiverModel
from pins import board_folder

b = board_folder('data/model', allow_pickle_read=True)
v = VetiverModel.from_pin(b, 'penguin_model')

app = VetiverAPI(v, check_prototype=True)

app.run(port = 8080)

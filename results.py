from flask_table import Table, Col

class Results(Table):
    id = Col('ID', show=False)
    name = Col('First Name')
    age = Col('Age')
    
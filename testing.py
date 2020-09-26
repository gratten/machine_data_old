from app import db
from app.models import Machine, Kit

m = Machine(project='HS5200')
m = Machine(serialnum='ENT-100')

# m = Machine(project='HS5200', serialnum='ENT-100',
#             customer='Sargento', description='opp hand')
# db.session.add(m)
# db.session.commit()
#
# m = Machine(project='HS5250', serialnum='ENT-OC-101',
#             customer='Schwanns', description='std hand')
# db.session.add(m)
# db.session.commit()
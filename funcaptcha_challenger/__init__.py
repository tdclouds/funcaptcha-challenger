from funcaptcha_challenger.match_count import ObjectCountPredictor
from funcaptcha_challenger.rotate_animal import AnimalRotationPredictor

arp = AnimalRotationPredictor()
predict_3d_rollball_animals = arp.predict

ocp = ObjectCountPredictor()
predict_numericalmatch = ocp.predict

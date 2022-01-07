import train
# train.train_and_save_model() # Uncomment to retrain the Model
import check_stress


#1 means normal and no stress
condition = check_stress.check_stress(50,37,600)
print(condition)
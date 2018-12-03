# demo_cal_elo

code snippet for calculating multi-player elo.

Once upon a time, i received a dataset of horse racing result from my friends. They want me to write a script to generate list of elo of the horse, trainer, and jockey.

This code snippet includes the basic implementation of the elo calulation for multiplayer.

I have used the packages for the elo calculationg, reference can be found at:
https://pypi.org/project/multi-elo/

Basically, I use dict to store the latest ELO of the participants (horse , trainer, and jockey). In each race, I will take their latest ELO out and update the ELO according to their finishing position in the race. The above process will recursively done until there is no race left in the list.

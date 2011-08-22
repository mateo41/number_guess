from django.db import models

# Create your models here.

class Game(models.Model):
    number = models.IntegerField()
    pub_date = models.DateTimeField('date played')


    def __unicode__(self):
        return unicode(self.number) 

    def get_tries(self):
        return len(self.guess_set.all())
    
    def status(self): 
        guesses = self.guess_set.all()  
        if len(guesses) == 0:
           return "Playing"
        last_guess = guesses[len(guesses) -1] 
        if last_guess.guess == self.number:
            return  "Won"
        if self.get_tries() > 4:
            return  "Lose"
        return "Playing"

class Guess(models.Model):
    game = models.ForeignKey(Game)
    guess = models.IntegerField()

    def __unicode__(self):
        return "Guess is %d on attempt %d" % (self.guess, self.game.get_tries())
    
    def guess_correct(self):
        return self.guess == self.game.number
   
    def guess_result(self):     
        if self.guess == self.game.number:
            return "correct"
        if self.guess < self.game.number:
            return "low"
        else:
            return "high"
   

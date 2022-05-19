import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
import pickle


def make_prediction(text):
    # loading
    with open('./tokenizer/tokenizer.pickle', 'rb') as handle:
        tokenizer = pickle.load(handle)

    max_length = 1000

    sequences = tokenizer.texts_to_sequences([text])
    train_sequence = pad_sequences(
        sequences, maxlen=max_length, value=0.0, padding='post')

    loaded_model = tf.keras.models.load_model('./saved_models')

    results = loaded_model.predict(train_sequence)
    # print(results)
    if results[0][0] > results[0][1]:
        return f'False news, {"{:.0%}".format(results[0][0])} certainty'
    elif results[0][1] > results[0][0]:
        return f'True news, {"{:.0%}".format(results[0][1])} certainty'


if __name__ != 'main':

    text = ''' But the couple, who have two primary-aged kids, carried on with their day like normal after realising they had won the EuroMillions.

Communications Sales Engineer Joe, who bought the winning Lucky Dip ticket just hours before the draw, didn't even wake up his wife after realising the win - waiting for her alarm to go off before whispering to Jess he had a "secret".

Jess called it a "normal husband-and-wife grumpy morning", adding: "Joe got up as usual at 5.15am to sort out the couple’s dogs. 

"Once the dogs were happy he checked his phone and saw the email from The National Lottery saying, ‘Good news, you’ve won a prize’. "Joe added: “I looked it up and saw we’d won.  I saw how much and I didn’t know what to do. 

"I couldn’t go back to sleep, I didn’t want to wake Jess up so I just laid there for what seemed like forever.

"I spent some time searching for property with no budget limit, which was a novelty!”

Joe has been married to hairdresser Jess for 11 years and they live in a £600,000 house with ponies, geckos, chickens and dogs. They celebrated the win with a family meal.Jess's mum thought she was pregnant when she was about to break the news. Jess told her: "It's better than being pregnant. I think we've won the lottery."

Her mum, who knew the prize pot down to the penny, screamed and burst into tears.

Jess added: "Even though it's wonderful and exciting, it's just a huge relief. We're just an ordinary family."

The couple want to spend the money on treats including a trip to Hawaii. Jess said: "The win gives us time to dream, which we haven't had before."

Joe said he always chooses the Lucky Dip as he thinks it is "easier", while Jess added: "My dad played the Lottery when we were growing up and he played the same numbers every single week.

The win gives us time to dream, which we haven't had before

Jess Thwaite
"He died about seven years ago and kind of Joe took on the baton as the one who did the Lottery for our family.

"So he started off using those numbers, but he'd forget them or get them wrong or something, so we then went to Lucky Dip, so that it was luck.

"But yeah it's unbelievable because that's what my dad dreamed of all his life, and used to say to us frequently 'Imagine if you won the Lottery, think about if you won the Lottery'.

"And yeah it's just crazy."

The previous highest winners stayed anonymous when they bagged £170million in October 2019.


12
And Colin and Chris Weir were next when they became Europe's second biggest lottery winners in July 2011.

They won £162million, putting them into The Sunday Times rich list above Beatle Ringo Starr and Sir Tom Jones.

Colin, who died in December 2019, spent £40million in eight years, including a £20,000 investment in bakery Greggs.

But the couple, of Largs, Ayshire, ended up divorcing in 2019 eight years after scooping the jackpot.

They were married for 38 years before being hit by the curse of the lottery.

Pals said it was an "open secret" they had drifted apart following their record-breaking win.

Colin and Chris Weir won £161million
12
Colin and Chris Weir won £161millionCredit: PA
Adrian and Gillian Bayford won £148million in 2012 but they spit up just 15 months later.

Gillian bought a lavish £1.2million mansion, launched a property business and snapped up a fleet of cars including a £150,000 Bentley Bentayga.

Her dad blasted her publicly, claiming she only gave him £1million rather than the £20million she claimed to have given.

In July, unlucky-in-love Adrian sold the £6million mansion where he was dumped four times.

The home had 189 acres, a cinema, billiards room, gym and a pool.

Adrian and Gillian Bayford won £148million
12
Adrian and Gillian Bayford won £148millionCredit: Rex
Frances and Patrick Connolly, of County Armagh, won £114.9million on the New Year's Day EuroMillions jackpot in 2019.

The retired teacher and businessman said one of the first things they did was sit down and write a list of 50 people they want to share the money with.

They then bought computers for children stuck at home who had no means of accessing an education during Covid lockdown.

And the pair proved the most generous of all winners when it was revealed they'd given away more than half of their cash to loved ones, charity and those in need during the pandemic.

In March Ruth and Mark Chalmers told how they used their £1million EuroMillions win to help daughters Natalie and Leanne have kids.

They also made sure they could support their new family by getting them on the property ladder mortgage-free.'''

    print(make_prediction(text))

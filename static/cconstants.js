// Options the user could type in
const prompts = [
  ["hi", "hey", "hello", "good morning", "good afternoon"],
  ["how are you", "how is life", "how are things"],
  ["what are you doing", "what is going on", "what is up"],
  ["how old are you"],
  ["who are you", "are you human", "are you bot", "are you human or bot"],
  ["who created you", "who made you"],
  ['what do you do'],
  [
    "your name please",
    "your name",
    "may i know your name",
    "what is your name",
    "what call yourself"
  ],
  ["love the app"],
  ["happy", "good", "fun", "wonderful", "fantastic", "cool"],
  ["bad", "bored", "tired"],
  ["help me"],
  ["bye", "good bye", "goodbye", "see you later"],
  ["ah", "yes", "ok", "okay", "nice"],
  ["what should i do"],
  ["bro"],
  ["what", "why", "how", "where", "when"],
  ["no","not sure","maybe","no thanks"],
  [""],
  ["what does diabetes prediction do","diabetes","predict diabetes","do I have diabetes"],
  ["heart disease","what does heart disease prediction do","predict heart disease","do I have a heart disease"],
  ["covid 19"],
  ["symptoms","covid symptoms","early covid 19 symptoms","cold","cough","corona","covid"],
  ["causes","covid causes","what causes covid 19 ","corona causes"],
  ["prevention","covid prevention","hand wash","mask","social distancing","prevention measures","corona prevention"]
]

// Possible responses, in corresponding order

const replies = [
  ["Hello!", "Hi!", "Hey!", "Hi there!","Howdy"],
  [
    "Fine... how are you?",
    "Pretty well, how are you?",
    "Fantastic, how are you?"
  ],
  [
    "Nothing much",
    "About to help you!",
    "Can you guess?",
    "I don't know, you tell me!"
  ],
  ["I am infinite"],
  ["I am just a bot names Geno", "I am Geno, a bot! What are you?"],
  ["Genometrics team!"],
  ["I am Geno and I can help guide you through our web application. The application has articles you can refer you and helps you by predicting if you have diabetes or heart disease. You can also ask me questions about covid and I will do my best to answer you!"],
  ["I am Geno", "Geno- The Friendly Bot"],
  ["I am so glad to hear that!", "I know right"],
  ["Have you ever felt bad?", "Glad to hear it"],
  ["How about I tell you what to do", "Why? You shouldn't! Try our diabetes prediction to change your mood", "Try reading articles on our website"],
  ["What about prediciting if you have a heart disease?", "Once upon a time... There was no app to predict diabetes and now there is."],
  ["Check out our website!", "How does reading articles sound?", "Wanna know about genes"],
  ["Bye", "Goodbye", "See you later"],
  ["Read our articles!", "Play our prediciton games!"],
  ["Bro!"],
  ["Great question, let me think"],
  ["That's ok","I understand","What do you want to talk about?"],
  ["Please say something :("],
  ["ok"],
  ["to predict diabetes we require information about you such as your family history of diabetes, your age, your BMI and so on. These values need to be entered as numeric values and our model will predict and tell you if you may are affected by it or not. "],
  ["for the prediction of heart disease basic information is not sufficient and we need a little more in deatiled information such as your cholestrol levels, resting ecg values and so on. This information can be acquired by visiting your nearest doctor for furthur information. "],
  ["Coronavirus disease 2019 (COVID-19) is a contagious disease caused by severe acute respiratory syndrome coronavirus 2 (SARS-CoV-2). The first known case was identified in Wuhan, China in December 2019.The disease has since spread worldwide, leading to an ongoing pandemic."],
  ["Symptoms of COVID-19 are variable, ranging from mild symptoms to severe illness.Common symptoms include headache, loss of smell and taste,  nasal congestion and runny nose, cough, muscle pain, sore throat, fever, diarrhea, and breathing difficulties."],
  ["The disease is mainly transmitted via the respiratory route when people inhale droplets and particles that infected people release as they breathe, talk, cough, sneeze, or sing. Infected people are more likely to transmit COVID-19 the when they are physically close. However, infection can occur over longer distances, particularly indoors. Infectivity begins as early as three days before symptoms appear, and people are most infectious just prior to and during the onset of symptoms. It declines after the first week, but infected people remain contagious for up to 20 days. People can spread the disease even if they are asymptomatic."],
  ["Without pandemic containment measures – such as social distancing, vaccination, and face masks – pathogens can spread exponentially. This graphic shows how early adoption of containment measures tends to protect wider swaths of the population. Preventive measures to reduce the chances of infection include getting vaccinated, staying at home, wearing a mask in public, avoiding crowded places, keeping distance from others, ventilating indoor spaces, managing potential exposure durations, washing hands with soap and water often and for at least twenty seconds, practising good respiratory hygiene, and avoiding touching the eyes, nose, or mouth with unwashed hands."]

]

// Random for any other user input

const alternative = [
  "Same",
  "Go on...",
  "Bro...",
  "Try again",
  "I'm listening...",
  "I don't understand :/"
]

// Whatever else you want :)

const coronavirus = ["Please stay home", "Wear a mask", "Fortunately, I don't have COVID", "These are uncertain times"]
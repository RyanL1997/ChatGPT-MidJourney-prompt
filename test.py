from chatGPTMidJourneyPrompt.mjPrompt import PromptGenerator

def runGPT(promptString):

  # supported authorization methods: via email and password, via token, via api key
  config = {
      "email": "your_email",
      "password": "your_password",
      # or
      "session_token": "your_session_token",
      # or
      "api_key": "api_keys_here",
  }
  
  # TODO: CHOOSE DIFFERENT VERISONS BASED ON USAGE REQUIREMENTS 
  promptGenerator = PromptGenerator(config)
  #prompt = promptGenerator.V5(promptString)
  #prompt = promptGenerator.V4(promptString)
  #prompt = promptGenerator.niji(promptString)
  #prompt = promptGenerator.testp(promptString)
  
  # or advanced usage if needed
  promptConfig = {
    "model": "artistic",
    "type": "anime",
    "renderer": "ray tracing",
    "content": "character",
    "aspect_ratio": "1:5",
    "color": "red",
    "url": "example image url",
  }
  
  # TODO: CHOOSE DIFFERENT VERISONS BASED ON USAGE REQUIREMENTS 
  prompt = promptGenerator.V5(promptString, config=promptConfig, words=50)
  print("\n==========The Prompt Starts Here==========\n")
  print(prompt)
  print("\n==========The Prompt Ends Here==========\n")


def main():
  # TODO: SUPPORT UTF-8 CHINESE CHARACTER SUPPORT
  promptString = input("Enter a prompt here: ")
  runGPT(promptString)

if __name__ == '__main__':
    main()
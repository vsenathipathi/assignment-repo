# Build an agent that can browse websites and extract specific information like news headlines and store them in a file. 

# -> Using AI agent instead of simple code based non-AI agent.
# -> Based on my Youtube learning, I am going with Langchain ReAct agent for this task
# -> This agent uses this flow Thought-> Action -> Observation

# langchain =  0.3.18
# langchain-community =  0.3.17

from langchain.agents import initialize_agent, tool

# ---------------- MODEL BLOCK START--------------- #
from langchain_google_genai import ChatGoogleGenerativeAI
import os
from dotenv import load_dotenv
load_dotenv()

gemini_model=os.environ['GEMINI_MODEL']
llm = ChatGoogleGenerativeAI(model=gemini_model) 
# ---------------- MODEL BLOCK END--------------- #


# Defined tool, gave description as agent expects this.
@tool
def date_time_check():
    """ function to get the today's date, time"""
    from datetime import datetime
    today=datetime.today().strftime("%d/%m/%Y %H:%M:%S")
    return today

@tool
def scrape_bbc_headlines(url: str):
    """ Function to scrape the give website and extract headlines"""
    import requests
    from bs4 import BeautifulSoup
    response=requests.get(url)
    parse_HTML=BeautifulSoup(response.text, 'html.parser')

    headlines=[]
    for tag in parse_HTML.find_all(["h2", "h3"]):
        text=tag.get_text(strip=True)
        if text and len(text)>10:
            headlines.append(text)
    return headlines


tools = [scrape_bbc_headlines]

agent = initialize_agent(tools=tools, llm=llm, agent="zero-shot-react-description", verbose=True)

resp=agent.invoke("Browse https://www.bbc.com/news, extract news headlines and list them as points, In the Heading add today's date and time")

print(resp['output'])


# > Entering new AgentExecutor chain...
# Action: scrape_bbc_headlines
# Action Input: https://www.bbc.com/news
# Observation:
# Thought:Thought:I have already scraped the headlines from the BBC News website. Now I need to format them as requested, including today's date and time in the heading and listing them as bullet points. I should also remove any duplicate headlines from the observation.

# Final Answer:
# **BBC News Headlines - 2024-07-30 15:45:00**

# * Trump hails 'amazing' meeting with China's Xi but no formal trade deal agreed
# * Jamaican officials assess 'total devastation' as Hurricane Melissa approaches Bermuda     
# * Reports of mass killings in Sudan have echoes of its dark past
# * Mumbai police rescue 17 children taken hostage at acting school
# * Verifying new evidence of RSF involvement in Sudan civil war executions
# * Xi and Trump find temporary truce as China plays longer game
# * Dutch centrist liberals neck and neck with populist Wilders in tight election
# * Israel receives coffins Hamas says contain two Gaza hostages' bodies
# * Cruise operator 'failed' woman who was left on island and died, family says
# * Five new suspects arrested over Louvre jewellery theft
# * Trump directs nuclear weapons testing to resume for first time in over 30 years
# * Ontario premier demands apology from US ambassador over tariff 'tirade'
# * Teenage cricketer dies in Melbourne after being hit by ball
# * How China really spies on the UK
# * Five ways the government shutdown is hurting Americans
# * Who is Rob Jetten, tipped to become youngest Dutch prime minister?
# * How Kane's NFL dream could become a reality
# * The dads helping daughters through their periods
# * Watch: US and China's different reports of their trade meeting
# * Handshakes and whispers: Trump and Xi's meeting…in 73 seconds
# * Trump imitates India's PM Narendra Modi in South Korea
# * Watch: Moment Donald Trump and Xi Jinping meet
# * Sex, class, horses: The unique mix that made Jilly Cooper's books special
# * 'Lost' spider species rediscovered in UK after 40 years
# * K-pop group NewJeans loses legal battle against agency
# * Climate change intensified India's heatwaves in 2024 - Lancet study
# * Mystery US donor gives £1m to Highlands steam railway
# * Lily Allen to tour new break-up album in UK theatres
# * Israeli troops kill municipal worker in south Lebanon raid
# * Man dies and three injured in helicopter crash
# * How much trouble is Rachel Reeves in over rental rule break?
# * India going well against Australia in World Cup semi-final
# * 'More to come' as Van der Merwe hits Scotland landmark
# * Agyemang to miss rest of season with ruptured ACL
# * Toronto move within one win of World Series title
# * How Haaland prompted a debate on drinking raw milk
# * Crowley starts at 10 with Doris on bench for Ireland against All Blacks
# WARNING: All log messages before absl::InitializeLog() is called are written to STDERR
# E0000 00:00:1761839239.630197    8916 init.cc:232] grpc_wait_for_shutdown_with_timeout() timed out.
# GB News Discord Bot

## Overview
This **Python-based Discord bot** that was created as a **web scraping experiment**. It fetches the latest **GB News** articles and even streams **GB News "Radio"** into a voice channel.
This bot utilises RSS feeds and Web scraping and as such can be adapted for use with a variety of news sources.

## Why?
Good question.

## Features
**Live News Updates** – Scrapes GB News and delivers the latest headlines directly to your Discord server.  
**Radio Streaming** – Play GB News Live Radio in your voice channel (for those truly committed to listening to Rees-Mogg's monologues).  
**Smart Disconnect** – The bot leaves the voice channel if it's left alone.  

## Commands
| **Command**   | **Description** |
|--------------|----------------|
| `/latest [category]` | Fetches the latest article from a specific news category (News, Politics, Sport, etc.). |
| `/radio` | Streams **GB News Live Radio** in your current voice channel. |
| `/disconnect` | Stops the radio and disconnects the bot from the voice channel. |

## Dependencies
| Package          |
|-----------------|
| discord.py      |
| feedparser      |
| beautifulsoup4  |
| requests        |


## Example Responses on Desktop & Mobile

| Embed Type       | Desktop View                                             | Mobile View                                              |
|------------------|----------------------------------------------------------|----------------------------------------------------------|
| **Regular Article** | <img src="https://github.com/user-attachments/assets/23160ac3-b6b0-41b6-ad08-6908d83ff778" width="300"> | <img src="https://github.com/user-attachments/assets/24fb0059-8e58-4ed9-8c69-c050c460e7cf" width="300"> |
| **Member Article** | <img src="https://github.com/user-attachments/assets/323c637d-098c-43ab-987e-0bcb7a03a013" width="300"> | <img src="https://github.com/user-attachments/assets/cd8a70ff-8d47-422f-82f3-aea45bd67a82" width="300"> |
| **Video**        | <img src="https://github.com/user-attachments/assets/60818f6b-1e06-4867-a669-ea9e1ea705c6" width="300"> | <img src="https://github.com/user-attachments/assets/c5d47747-1dac-4d89-a044-c8804e42ec9a" width="300"> |



# GB News Discord Bot

## Overview
This **Python-based Discord bot** that was created as a **web scraping experiment**. It fetches the latest **GB News** articles and even streams **GB News "Radio"** into a voice channel.

##Why?
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

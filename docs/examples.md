# Examples

Comprehensive examples for using PopcatAPI Wrapper in real applications.

## Discord Bot Integration

### Basic Meme Bot

```python
import discord
from discord.ext import commands
import popcatapi_wrapper as popcat

bot = commands.Bot(command_prefix='!')

@bot.command()
async def drake(ctx, *, text):
    """Generate Drake meme with custom text"""
    if ' | ' in text:
        text1, text2 = text.split(' | ', 1)
        meme_url = popcat.drake(text1, text2)
        
        embed = discord.Embed(title="Drake Meme")
        embed.set_image(url=meme_url)
        await ctx.send(embed=embed)
    else:
        await ctx.send("Usage: `!drake text1 | text2`")

@bot.command()
async def weather(ctx, *, location):
    """Get weather information"""
    try:
        weather_data = popcat.weather(location)
        
        embed = discord.Embed(
            title=f"Weather in {weather_data['location']}",
            color=0x3498db
        )
        embed.add_field(name="Temperature", value=weather_data['temperature'])
        embed.add_field(name="Condition", value=weather_data['condition'])
        embed.add_field(name="Humidity", value=weather_data['humidity'])
        
        await ctx.send(embed=embed)
    except Exception as e:
        await ctx.send(f"Error getting weather: {e}")

bot.run('YOUR_BOT_TOKEN')
```

### Advanced Image Processing Bot

```python
@bot.command()
async def jail(ctx, user: discord.Member = None):
    """Put someone in jail"""
    if user is None:
        user = ctx.author
    
    avatar_url = str(user.avatar.url)
    jail_image = popcat.jail(avatar_url)
    
    embed = discord.Embed(title=f"{user.display_name} is in jail! 🔒")
    embed.set_image(url=jail_image)
    await ctx.send(embed=embed)

@bot.command()
async def ship(ctx, user1: discord.Member, user2: discord.Member):
    """Ship two users together"""
    avatar1 = str(user1.avatar.url)
    avatar2 = str(user2.avatar.url)
    
    ship_image = popcat.ship(avatar1, avatar2)
    
    embed = discord.Embed(
        title=f"💕 {user1.display_name} x {user2.display_name}",
        description="Let's see how compatible they are!"
    )
    embed.set_image(url=ship_image)
    await ctx.send(embed=embed)
```

## Web Application

### Flask API Server

```python
from flask import Flask, jsonify, request
import popcatapi_wrapper as popcat

app = Flask(__name__)

@app.route('/api/meme/drake', methods=['POST'])
def create_drake_meme():
    data = request.get_json()
    
    if not data or 'text1' not in data or 'text2' not in data:
        return jsonify({'error': 'text1 and text2 required'}), 400
    
    try:
        meme_url = popcat.drake(data['text1'], data['text2'])
        return jsonify({'meme_url': meme_url})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/weather/<location>')
def get_weather(location):
    try:
        weather_data = popcat.weather(location)
        return jsonify(weather_data)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/random')
def random_content():
    try:
        content = {
            'joke': popcat.joke(),
            'fact': popcat.fact(),
            'color': popcat.randomcolor(),
            'showerthought': popcat.showerthought()
        }
        return jsonify(content)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
```

### FastAPI Implementation

```python
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import popcatapi_wrapper as popcat

app = FastAPI(title="PopcatAPI Wrapper API")

class DrakeMemeRequest(BaseModel):
    text1: str
    text2: str

class QuoteRequest(BaseModel):
    image_url: str
    text: str
    name: str

@app.post("/meme/drake")
async def create_drake_meme(request: DrakeMemeRequest):
    try:
        meme_url = popcat.drake(request.text1, request.text2)
        return {"meme_url": meme_url}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/meme/quote")
async def create_quote(request: QuoteRequest):
    try:
        quote_url = popcat.quote(request.image_url, request.text, request.name)
        return {"quote_url": quote_url}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/weather/{location}")
async def get_weather(location: str):
    try:
        weather_data = popcat.weather(location)
        return weather_data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
```

## Data Analysis

### GitHub User Analysis

```python
import popcatapi_wrapper as popcat
import pandas as pd
import matplotlib.pyplot as plt

def analyze_github_users(usernames):
    """Analyze multiple GitHub users"""
    users_data = []
    
    for username in usernames:
        try:
            data = popcat.github(username)
            users_data.append({
                'username': data['username'],
                'followers': data['followers'],
                'public_repos': data['public_repos'],
                'following': data['following']
            })
        except Exception as e:
            print(f"Error fetching {username}: {e}")
    
    df = pd.DataFrame(users_data)
    
    # Create visualization
    fig, axes = plt.subplots(2, 2, figsize=(12, 10))
    
    # Followers distribution
    axes[0, 0].bar(df['username'], df['followers'])
    axes[0, 0].set_title('Followers Count')
    axes[0, 0].tick_params(axis='x', rotation=45)
    
    # Repositories count
    axes[0, 1].bar(df['username'], df['public_repos'])
    axes[0, 1].set_title('Public Repositories')
    axes[0, 1].tick_params(axis='x', rotation=45)
    
    # Following count
    axes[1, 0].bar(df['username'], df['following'])
    axes[1, 0].set_title('Following Count')
    axes[1, 0].tick_params(axis='x', rotation=45)
    
    # Follower to following ratio
    df['ratio'] = df['followers'] / (df['following'] + 1)
    axes[1, 1].bar(df['username'], df['ratio'])
    axes[1, 1].set_title('Follower/Following Ratio')
    axes[1, 1].tick_params(axis='x', rotation=45)
    
    plt.tight_layout()
    plt.show()
    
    return df

# Usage
users = ['octocat', 'torvalds', 'gaearon', 'sindresorhus']
results = analyze_github_users(users)
print(results)
```

### Weather Dashboard

```python
import popcatapi_wrapper as popcat
import streamlit as st
import plotly.graph_objects as go

def create_weather_dashboard():
    st.title("🌤️ Weather Dashboard")
    
    # Sidebar for city input
    st.sidebar.header("Settings")
    cities = st.sidebar.multiselect(
        "Select cities:",
        ["London", "New York", "Tokyo", "Paris", "Sydney", "Dubai"],
        default=["London", "New York", "Tokyo"]
    )
    
    if cities:
        weather_data = []
        
        for city in cities:
            try:
                data = popcat.weather(city)
                weather_data.append({
                    'City': city,
                    'Temperature': data['temperature'],
                    'Condition': data['condition'],
                    'Humidity': data['humidity']
                })
            except Exception as e:
                st.error(f"Error fetching weather for {city}: {e}")
        
        if weather_data:
            df = pd.DataFrame(weather_data)
            
            # Display weather cards
            cols = st.columns(len(cities))
            for i, (_, row) in enumerate(df.iterrows()):
                with cols[i]:
                    st.metric(
                        label=row['City'],
                        value=row['Temperature'],
                        delta=row['Condition']
                    )
                    st.write(f"💧 Humidity: {row['Humidity']}")

if __name__ == "__main__":
    create_weather_dashboard()
```

## Automation Scripts

### Daily Content Generator

```python
import popcatapi_wrapper as popcat
import schedule
import time
from datetime import datetime

def generate_daily_content():
    """Generate daily content for social media"""
    
    # Get random content
    joke = popcat.joke()
    fact = popcat.fact()
    color = popcat.randomcolor()
    showerthought = popcat.showerthought()
    
    # Create a daily summary
    content = f"""
🌅 Daily Content - {datetime.now().strftime('%Y-%m-%d')}

😂 Joke of the Day:
{joke}

🧠 Random Fact:
{fact}

🎨 Color of the Day:
{color['name']} ({color['hex']})

💭 Shower Thought:
{showerthought['thought']}
    """
    
    print(content)
    
    # You could save to file, post to social media, etc.
    with open(f"daily_content_{datetime.now().strftime('%Y%m%d')}.txt", "w") as f:
        f.write(content)

# Schedule the function
schedule.every().day.at("09:00").do(generate_daily_content)

# Keep the script running
while True:
    schedule.run_pending()
    time.sleep(1)
```

### Bulk Image Processing

```python
import popcatapi_wrapper as popcat
import os
from concurrent.futures import ThreadPoolExecutor
import time

def process_image(image_url, effects=['jail', 'blur', 'greyscale']):
    """Apply multiple effects to an image"""
    results = {}
    
    for effect in effects:
        try:
            if effect == 'jail':
                results[effect] = popcat.jail(image_url)
            elif effect == 'blur':
                results[effect] = popcat.blur(image_url)
            elif effect == 'greyscale':
                results[effect] = popcat.greyscale(image_url)
            elif effect == 'drip':
                results[effect] = popcat.drip(image_url)
            elif effect == 'clown':
                results[effect] = popcat.clown(image_url)
            
            # Add delay to respect rate limits
            time.sleep(0.5)
            
        except Exception as e:
            print(f"Error applying {effect} to {image_url}: {e}")
            results[effect] = None
    
    return results

def bulk_process_images(image_urls, max_workers=3):
    """Process multiple images concurrently"""
    
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = {executor.submit(process_image, url): url for url in image_urls}
        
        results = {}
        for future in futures:
            url = futures[future]
            try:
                results[url] = future.result()
                print(f"✅ Processed: {url}")
            except Exception as e:
                print(f"❌ Failed: {url} - {e}")
                results[url] = None
    
    return results

# Usage
image_urls = [
    "https://example.com/image1.jpg",
    "https://example.com/image2.jpg", 
    "https://example.com/image3.jpg"
]

processed = bulk_process_images(image_urls)
for url, effects in processed.items():
    print(f"\n{url}:")
    for effect, result_url in effects.items():
        print(f"  {effect}: {result_url}")
```

import random
import time

# List of tarot cards and their descriptions
cards = {
    "The Fool": "A new beginning, a leap of faith, innocence. ✨ A reminder that sometimes taking a risk can lead to great rewards. Trust the journey.",
    "The Magician": "Manifestation, resourcefulness, power. 💪 You have the tools to succeed. Harness your inner power and make things happen.",
    "The High Priestess": "Intuition, unconscious knowledge, mystery. 🌙 Listen to your inner voice; the answers you seek are already within you.",
    "The Empress": "Abundance, nurturing, fertility, creativity. 🌸 Nurture your ideas, and they will grow into something beautiful and fulfilling.",
    "The Emperor": "Authority, structure, stability, leadership. 🏛️ Take charge of your situation; your leadership will bring order and stability.",
    "The Hierophant": "Tradition, spiritual guidance, conformity. 📜 Seek wisdom from trusted sources, but remember that growth often requires breaking away from tradition.",
    "The Lovers": "Love, union, choices, harmony. 💖 This is a time to connect deeply with others or make choices that align with your true desires.",
    "The Chariot": "Victory, control, determination, willpower. 🏆 Keep your focus and determination, success is within your reach.",
    "Strength": "Courage, strength, patience, inner power. 💪 Embrace challenges with patience; your inner strength will guide you through.",
    "The Hermit": "Solitude, reflection, guidance from within. 🌿 Take time for introspection; clarity will come from within when you step away from the noise.",
    "Wheel of Fortune": "Change, cycles, destiny, luck. 🔄 Embrace the natural flow of life—what goes down will come back up. Stay adaptable.",
    "Justice": "Fairness, balance, truth, cause and effect. ⚖️ Trust that justice will prevail, and your actions will have the consequences they deserve.",
    "The Hanged Man": "Suspension, letting go, new perspectives. 🌀 Sometimes, the best way forward is to let go and see things from a new angle.",
    "Death": "Endings, transformation, rebirth. 💀 Every ending brings a new beginning. Embrace transformation and the opportunity for renewal.",
    "Temperance": "Balance, moderation, purpose, healing. ⚖️ Seek balance in your life; moderation will lead to peace and progress.",
    "The Devil": "Temptation, addiction, materialism, bondage. ⛓️ Be mindful of unhealthy attachments. Freedom comes from letting go of what binds you.",
    "The Tower": "Sudden change, chaos, awakening. 🌪️ Expect the unexpected; sometimes chaos is necessary to clear the path for new opportunities.",
    "The Star": "Hope, inspiration, faith, renewal. 🌟 Stay hopeful, even in dark times. Your dreams and aspirations are within reach.",
    "The Moon": "Illusion, intuition, dreams, the subconscious. 🌙 Trust your instincts, but be cautious—things may not be what they seem.",
    "The Sun": "Success, vitality, joy, enlightenment. 🌞 A time of joy and success is ahead. Let your positivity and energy shine.",
    "Judgment": "Rebirth, inner calling, reflection, absolution. 🔔 Reflect on your past actions and embrace a new chapter of growth and understanding.",
    "The World": "Completion, achievement, fulfillment, wholeness. 🌍 The cycle is complete. You've come full circle and are ready for the next adventure."
}

# Introduction and instructions
print("\n🌟 Welcome to Charmed Code, your Tarot Reading! 🌟\n")
time.sleep(2)
print("Before we begin, take a moment to clear your mind. 🧘‍♀️")
time.sleep(3)
print("Focus on a question you'd like to ask the universe. 💭")
time.sleep(2)
print("\nWhen you're ready, we'll shuffle the deck. 🌿")
time.sleep(4)

# Ask how many cards to draw
while True:
    try:
        num_cards = int(input("\nHow many cards would you like to draw? (1-5): "))
        if 1 <= num_cards <= 5:
            break
        else:
            print("Please choose a number between 1 and 5.")
    except ValueError:
        print("That's not a valid number. Please enter a number between 1 and 5.")

# Time to shuffle the cards
print("\nShuffling the cards... 🔮")
time.sleep(2)

# Draw random cards
random_cards = random.sample(list(cards.items()), num_cards)

# Tarot reading result
print("\nYour tarot reading is: ✨")
time.sleep(1)

# Show each card with a small delay
for i, (card, description) in enumerate(random_cards, 1):
    print(f"\nCard {i}: {card} 🌟")
    time.sleep(1)
    print(f"{description}")
    time.sleep(1)

# Final message
print("\nRemember, the cards offer guidance, but your destiny is shaped by your choices. 🌌")
time.sleep(2)
print("The universe is listening to you. 💫")

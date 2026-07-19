import streamlit as st

# Configure the page for a clean mobile-first view
st.set_page_config(
    page_title="T1D School Routine",
    page_icon="🍏",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Custom Styling to match the color-coding rules
st.markdown("""
<style>
    .main-title { font-size: 24px; font-weight: bold; color: #1a365d; text-align: center; margin-bottom: 5px; }
    .subtitle { font-size: 14px; color: #4a5568; text-align: center; margin-bottom: 20px; font-style: italic; }
    .card-green { background-color: #e6fffa; border-left: 5px solid #234e52; padding: 12px; border-radius: 4px; margin-bottom: 10px; }
    .card-yellow { background-color: #fffaf0; border-left: 5px solid #744210; padding: 12px; border-radius: 4px; margin-bottom: 10px; }
    .card-orange { background-color: #fff5f5; border-left: 5px solid #742a2a; padding: 12px; border-radius: 4px; margin-bottom: 10px; }
    .badge-text { font-weight: bold; font-size: 12px; }
</style>
""", unsafe_style_html=True)

# App Header
st.markdown('<div class="main-title">🎒 Back-to-School T1D Planner</div>', unsafe_style_html=True)
st.markdown('<div class="subtitle">Predictable Carbs & Smart-Dosing for the Omnipod 5</div>', unsafe_style_html=True)

# Shared Database of Meals
meal_db = {
    "🌅 Breakfast": [
        {"name": "Power Omelet & Avocado", "portion": "2 Eggs, spinach, cheese, 1/4 avocado", "carbs": "2g (Fiber Complex)", "type": "Green", "guide": "No manual bolus required. Let the pump maintain a safe baseline."},
        {"name": "PB & Banana Oatmeal", "portion": "1/2 cup rolled oats, 1 tbsp PB, 1/2 banana", "carbs": "35g (Slow Burning)", "type": "Yellow", "guide": "Bolus 10 mins before eating to perfectly match the slow carbohydrate absorption."},
        {"name": "Greek Yogurt & Berries", "portion": "3/4 cup plain Greek yogurt + 1/2 cup berries", "carbs": "12g (Low Glycemic)", "type": "Green", "guide": "Light manual bolus, or let automated mode handle it if he is highly active active right after."}
    ],
    "🏫 School Lunch": [
        {"name": "Turkey & Cheese Wrap", "portion": "Low-carb tortilla, deli turkey, cheese, mustard", "carbs": "5g (Ultra-Low)", "type": "Green", "guide": "Great if lunch period is short or rushed; zero math or controller entry required."},
        {"name": "Classic Fuel Sandwich", "portion": "Whole wheat bread, chicken breast, lettuce, side of carrots", "carbs": "30g (Complex)", "type": "Yellow", "guide": "Bolus at the start of the lunch period. High fiber content helps prevent sharp spikes."},
        {"name": "Athlete Pasta Bowl", "portion": "1 cup whole grain pasta with marinara & grilled chicken", "carbs": "45g (High Load)", "type": "Orange", "guide": "Pre-bolus a full 15 minutes before eating to give the insulin a head start against high carb loads."}
    ],
    "🏠 Dinner": [
        {"name": "Grilled Chicken & Broccoli", "portion": "6oz Chicken breast, large side of broccoli with butter", "carbs": "6g (Fiber-Rich)", "type": "Green", "guide": "Ideal for a clean slate night. Gives the algorithm a perfect canvas to hit that 110 target overnight."},
        {"name": "Taco Night (Corn Tortillas)", "portion": "2 corn tortillas, lean beef, cheese, pico de gallo", "carbs": "24g (Moderate)", "type": "Yellow", "guide": "Bolus accurately. Keep an eye out for delayed protein/fat trend line rises 3-4 hours later."},
        {"name": "Burger & Sweet Potato Fries", "portion": "Turkey/Beef burger (lettuce wrap) + 1 cup baked sweet potato fries", "carbs": "28g (Sustained)", "type": "Orange", "guide": "Sweet potatoes digest slower than regular fries. Enter carbs precisely at the start of the meal."}
    ],
    "🌙 Snacks & Sports": [
        {"name": "String Cheese & Almonds", "portion": "1-2 sticks of cheese + a handful of almonds", "carbs": "2g (Zero Impact)", "type": "Green", "guide": "LATE NIGHT CRUSH: DO NOT BOLUS. Let the pump cruise smoothly down to his 110 target overnight."},
        {"name": "Apple Slices & Peanut Butter", "portion": "1 medium apple + 2 tbsp peanut butter", "carbs": "20g (Sustained)", "type": "Yellow", "guide": "After-School Study Session: Bolus required. Peanut butter helps slow down the natural fruit sugar spike."},
        {"name": "Athletic Fuel / Chocolate Milk", "portion": "1 cup (8 oz) chocolate milk", "carbs": "26g (Fast Release)", "type": "Orange", "guide": "Pre-Practice: Take 15-30 mins before intense workouts. Consider activating the pump's Activity Feature."}
    ]
}

# Step 1: Filter by Time of Day
time_category = st.selectbox("📅 Choose Time of Day:", list(meal_db.keys()))

# Step 2: Filter by Dosing Strategy (Color)
strategy_filter = st.radio(
    "💡 Filter by Dosing Type:",
    ["All Meals", "🟢 Green (No-Bolus / Low Carb)", "🟡 Yellow (Steady / Complex)", "🔴 Orange (Fast Carbs / Athletic)"]
)

st.markdown("---")

# Filter logic mapping
color_map = {
    "🟢 Green (No-Bolus / Low Carb)": "Green",
    "🟡 Yellow (Steady / Complex)": "Yellow",
    "🔴 Orange (Fast Carbs / Athletic)": "Orange"
)

# Display Meals
filtered_meals = meal_db[time_category]
visible_meals = 0

for meal in filtered_meals:
    # Apply type filter if selected
    if strategy_filter != "All Meals" and meal["type"] != color_map[strategy_filter]:
        continue
        
    visible_meals += 1
    
    # Determine look based on color type
    if meal["type"] == "Green":
        style_class = "card-green"
        badge = "🟢 NO-BOLUS CRUISE"
    elif meal["type"] == "Yellow":
        style_class = "card-yellow"
        badge = "🟡 STEADY COMPLEX CARB"
    else:
        style_class = "card-orange"
        badge = "🔴 ACTION REQUIRED"
        
    # Render Custom Card UI
    st.markdown(f"""
    <div class="{style_class}">
        <div style="display: flex; justify-content: space-between; align-items: center;">
            <strong style="font-size: 16px;">{meal['name']}</strong>
            <span class="badge-text">{badge}</span>
        </div>
        <div style="font-size: 13px; color: #4a5568; margin-top: 4px;"><strong>Portion:</strong> {meal['portion']}</div>
        <div style="font-size: 13px; color: #4a5568;"><strong>Carbs:</strong> {meal['carbs']}</div>
        <div style="font-size: 13px; color: #2d3748; margin-top: 6px; border-top: 1px dashed rgba(0,0,0,0.1); padding-top: 4px;">
            ℹ️ <strong>Pump Dosing Advice:</strong> {meal['guide']}
        </div>
    </div>
    """, unsafe_style_html=True)

if visible_meals == 0:
    st.info("No meals matching this color filter for this time block. Try choosing another category above!")

# Master Strategy Reminder Footnote
st.markdown("---")
st.info("💡 Pro Tip: To beat that 125 mg/dL overnight stall, guide him toward the 🟢 Green snack choices if he wants to eat close to bedtime.")

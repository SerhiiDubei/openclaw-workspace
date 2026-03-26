"""
MCS (Multi-Consciousness System) — Емуляція архітектури
Приклад роботи з 4 personas: Protector, Instinct, Thinker, Mask

Цей файл можна запустити для демонстрації роботи системи.
"""

import json
import math
from dataclasses import dataclass, field
from typing import Dict, List, Optional, Tuple
from enum import Enum


class DeltaCategory(Enum):
    EXPLOSIVE = "🔥🔥🔥"  # >60
    RAPID = "🔥▲"        # 30-60
    GRADUAL = "▲"        # 10-30
    STABLE = "—"         # <10


@dataclass
class PersonaState:
    """Стан однієї personas в конкретний момент"""
    id: str
    weight: float  # 0.0 - 1.0
    delta: float   # Зміна від попереднього стану
    delta_cat: DeltaCategory
    whisper: str
    
    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "weight": round(self.weight, 2),
            "delta": round(self.delta, 2),
            "delta_category": self.delta_cat.value,
            "whisper": self.whisper
        }


@dataclass
class Event:
    """Подія, що активує систему"""
    type: str
    intensity: float  # 0.0 - 1.0
    target: Optional[str] = None
    context: Dict = field(default_factory=dict)
    
    def to_dict(self) -> dict:
        return {
            "type": self.type,
            "intensity": self.intensity,
            "target": self.target,
            "context": self.context
        }


class Persona:
    """Базовий клас для однієї personas"""
    
    def __init__(self, 
                 persona_id: str, 
                 name: str,
                 core_inputs: Dict[str, str],
                 stat_modifiers: Dict[str, int],
                 triggers: Dict,
                 whispers: Dict[str, List[str]]):
        self.id = persona_id
        self.name = name
        self.core_inputs = core_inputs
        self.stat_modifiers = stat_modifiers
        self.triggers = triggers
        self.whispers = whispers
        
        # Internal memory
        self.times_activated = 0
        self.last_trigger = None
    
    def evaluate(self, event: Event, core_data: Dict) -> float:
        """
        Оцінює, наскільки ця persona реагує на подію.
        Повертає score 0.0 - 1.0
        """
        score = 0.0
        
        # 1. Instant triggers
        if event.type in self.triggers.get("instant", []):
            score += 0.8 * event.intensity
        
        # 2. Core inputs modifiers
        for stat, path in self.core_inputs.items():
            value = self._get_nested_value(core_data, path)
            if value and isinstance(value, (int, float)):
                # Нормалізуємо до 0-1 і додаємо до score
                normalized = value / 100.0
                score += normalized * 0.15
        
        # 3. Context modifiers
        if "public" in event.context and event.context["public"]:
            # Для деяких personas публічність важлива
            if self.id in ["mask", "protector"]:
                score += 0.1
        
        # 4. Suppressors
        for suppressor in self.triggers.get("suppressors", []):
            if self._check_condition(suppressor, core_data):
                score *= 0.3
        
        return min(score, 1.0)
    
    def generate_whisper(self, weight: float, delta: float) -> str:
        """Генерує внутрішній голос залежно від ваги та дельти"""
        
        # Вибираємо базовий шаблон
        if weight > 0.5:
            base = self.whispers["dominant"][0]
        elif weight > 0.2:
            base = self.whispers["secondary"][0]
        else:
            base = self.whispers.get("faint", ["..."])[0]
        
        # Delta модифікатор
        if delta > 0.6:
            return f"[ШОК] {base} Що відбувається?!"
        elif delta > 0.3:
            return f"[Наростає] {base}"
        elif delta < -0.3:
            return f"[Спадає] {base}..."
        else:
            return base
    
    def _get_nested_value(self, data: Dict, path: str):
        """Отримує значення за шляхом типу 'stats.energy'"""
        keys = path.split(".")
        current = data
        for key in keys:
            if isinstance(current, dict) and key in current:
                current = current[key]
            else:
                return None
        return current
    
    def _check_condition(self, condition: str, core_data: Dict) -> bool:
        """Перевіряє умову типу 'energy < 20'"""
        # Спрощена реалізація
        if "energy" in condition and "<" in condition:
            parts = condition.split("<")
            if len(parts) == 2:
                stat = parts[0].strip()
                threshold = float(parts[1].strip())
                value = self._get_nested_value(core_data, f"stats.{stat}")
                if value is not None:
                    return value < threshold
        return False


class TickProcessor:
    """Головний процесор тіків"""
    
    def __init__(self, npc_id: str, personas: List[Persona]):
        self.npc_id = npc_id
        self.personas = {p.id: p for p in personas}
        self.previous_weights = {p.id: 0.25 for p in personas}
        self.current_weights = {p.id: 0.25 for p in personas}
        self.tick_count = 0
    
    def tick(self, event: Event, core_data: Dict) -> Dict:
        """
        Обробляє один tick системи.
        Повертає повний стан після обробки.
        """
        self.tick_count += 1
        
        # 1. Кожна persona оцінює подію
        scores = {}
        for pid, persona in self.personas.items():
            scores[pid] = persona.evaluate(event, core_data)
        
        # 2. Softmax нормалізація
        new_weights = self._softmax(scores)
        
        # 3. Інерція (blend з попереднім станом)
        alpha = 0.7  # 70% нове, 30% інерція
        blended_weights = {
            pid: alpha * new_weights[pid] + (1 - alpha) * self.previous_weights[pid]
            for pid in new_weights
        }
        
        # 4. Розрахунок Delta
        deltas = {}
        delta_categories = {}
        for pid in blended_weights:
            delta = blended_weights[pid] - self.previous_weights[pid]
            deltas[pid] = delta
            delta_categories[pid] = self._categorize_delta(abs(delta))
        
        # 5. Генерація whispers
        persona_states = {}
        for pid in blended_weights:
            persona = self.personas[pid]
            whisper = persona.generate_whisper(blended_weights[pid], deltas[pid])
            persona_states[pid] = PersonaState(
                id=pid,
                weight=blended_weights[pid],
                delta=deltas[pid],
                delta_cat=delta_categories[pid],
                whisper=whisper
            )
        
        # 6. Оновлення стану
        self.previous_weights = self.current_weights.copy()
        self.current_weights = blended_weights
        
        # 7. Розрахунок модифікованих stats
        modified_stats = self._calculate_stats(core_data, blended_weights)
        
        # 8. Meta-output
        dominant = max(blended_weights, key=blended_weights.get)
        
        return {
            "npc_id": self.npc_id,
            "tick": self.tick_count,
            "event": event.to_dict(),
            "personas": {pid: state.to_dict() for pid, state in persona_states.items()},
            "weights": {pid: round(w, 3) for pid, w in blended_weights.items()},
            "deltas": {pid: round(d, 3) for pid, d in deltas.items()},
            "modified_stats": modified_stats,
            "dominant": dominant,
            "expression": self._generate_expression(persona_states, dominant)
        }
    
    def _softmax(self, scores: Dict[str, float]) -> Dict[str, float]:
        """Softmax нормалізація"""
        exp_scores = {pid: math.exp(s) for pid, s in scores.items()}
        sum_exp = sum(exp_scores.values())
        return {pid: s / sum_exp for pid, s in exp_scores.items()}
    
    def _categorize_delta(self, delta: float) -> DeltaCategory:
        """Категоризація різкості зміни"""
        delta_pct = abs(delta) * 100
        if delta_pct > 60:
            return DeltaCategory.EXPLOSIVE
        elif delta_pct > 30:
            return DeltaCategory.RAPID
        elif delta_pct > 10:
            return DeltaCategory.GRADUAL
        else:
            return DeltaCategory.STABLE
    
    def _calculate_stats(self, core_data: Dict, weights: Dict[str, float]) -> Dict:
        """Розраховує модифіковані stats на основі ваг personas"""
        base_stats = core_data.get("stats", {})
        result = base_stats.copy()
        
        # Для кожного stat застосовуємо модифікатори personas
        for pid, persona in self.personas.items():
            w = weights[pid]
            for stat, modifier in persona.stat_modifiers.items():
                if stat in result:
                    result[stat] += modifier * w
                else:
                    result[stat] = 50 + modifier * w  # База 50
        
        # Капаємо в 0-100
        for stat in result:
            result[stat] = max(0, min(100, int(result[stat])))
        
        return result
    
    def _generate_expression(self, states: Dict[str, PersonaState], dominant: str) -> Dict:
        """Генерує expression на основі станів"""
        dom_state = states[dominant]
        
        speech_styles = {
            "protector": "твердий, захисний",
            "instinct": "імпульсивний, емоційний",
            "thinker": "виміряний, аналітичний",
            "mask": "згладжений, соціально прийнятний"
        }
        
        body_lang = {
            "protector": "між загрозою і захищаємим",
            "instinct": "тремтіння або напруга",
            "thinker": "спокійна поза, оцінюючий погляд",
            "mask": "контрольована, усмішка або нейтралітет"
        }
        
        return {
            "dominant_persona": dominant,
            "speech_style": speech_styles.get(dominant, "нейтральний"),
            "body_language": body_lang.get(dominant, "спокійний"),
            "emotional_quality": f"{dominant} на {int(dom_state.weight * 100)}%"
        }


def create_katerina_personas() -> List[Persona]:
    """Створює 4 personas для Катерини"""
    
    protector = Persona(
        persona_id="protector",
        name="Захисник",
        core_inputs={
            "loyalty": "values.loyalty",
            "family": "values.family"
        },
        stat_modifiers={
            "courage": +30,
            "aggression": +20,
            "empathy": -10
        },
        triggers={
            "instant": ["loved_one_threatened", "boundary_violated", "injustice_witnessed"],
            "suppressors": ["energy < 20", "fear > 80"]
        },
        whispers={
            "dominant": ["Не піду, поки вони в безпеці.", "Вона під моїм захистом."],
            "secondary": ["Пильнуй за ними.", "Будь готовий."],
            "faint": ["Пильнуй..."]
        }
    )
    
    instinct = Persona(
        persona_id="instinct",
        name="Інстинкт",
        core_inputs={
            "energy": "stats.energy",
            "stress": "stats.stress"
        },
        stat_modifiers={
            "aggression": +40,
            "courage": +10,
            "rationality": -30
        },
        triggers={
            "instant": ["pain", "fear_stimulus", "provocation"],
            "suppressors": ["discipline_training"]
        },
        whispers={
            "dominant": ["Біжи! Зараз!", "Вдарити. Негайно."],
            "secondary": ["Щось не так...", "Напруга..."],
            "faint": ["Обережно..."]
        }
    )
    
    thinker = Persona(
        persona_id="thinker",
        name="Мислитель",
        core_inputs={
            "intelligence": "stats.intelligence"
        },
        stat_modifiers={
            "rationality": +40,
            "aggression": -20,
            "patience": +30
        },
        triggers={
            "instant": ["complex_problem", "moral_dilemma"],
            "suppressors": ["time_pressure", "extreme_emotion"]
        },
        whispers={
            "dominant": ["Якщо А, то Б. Якщо Б, то втрата.", "Проаналізуй."],
            "secondary": ["Потрібно більше даних.", "Подумай."],
            "faint": ["Цікаво..."]
        }
    )
    
    mask = Persona(
        persona_id="mask",
        name="Маска",
        core_inputs={
            "social_intelligence": "stats.social_intelligence"
        },
        stat_modifiers={
            "tact": +30,
            "authenticity": -20,
            "calm": +20
        },
        triggers={
            "instant": ["social_gathering", "authority_present", "public_attention"],
            "suppressors": ["trust_established", "extreme_emotion_override"]
        },
        whispers={
            "dominant": ["Вони не мають цього знати.", "Усміхнись. Притворись."],
            "secondary": ["Як це виглядає?", "Що вони думають?"],
            "faint": ["Будь ввічливим..."]
        }
    )
    
    return [protector, instinct, thinker, mask]


def create_katerina_core() -> Dict:
    """Створює CORE дані для Катерини"""
    return {
        "name": "Катерина",
        "stats": {
            "aggression": 50,
            "courage": 60,
            "empathy": 70,
            "rationality": 65,
            "energy": 80,
            "intelligence": 75,
            "social_intelligence": 60
        },
        "values": {
            "loyalty": 85,
            "family": 90,
            "honor": 70
        },
        "trauma": {
            "betrayed_by_friend": True,
            "lost_someone": False
        }
    }


def render_hud(state: Dict) -> str:
    """Рендерить візуальний HUD"""
    lines = []
    lines.append("=" * 60)
    lines.append(f"NPC: {state['npc_id']} | Tick #{state['tick']}")
    lines.append("=" * 60)
    lines.append("")
    
    # Event
    event = state['event']
    lines.append(f"📢 ПОДІЯ: {event['type']} (інтенсивність: {event['intensity']})")
    lines.append("")
    
    # Personas
    lines.append("🎭 PERSONAS:")
    for pid, pstate in state['personas'].items():
        weight_bar = "█" * int(pstate['weight'] * 10) + "░" * (10 - int(pstate['weight'] * 10))
        delta_sign = "▲" if pstate['delta'] > 0 else "▼" if pstate['delta'] < 0 else "—"
        lines.append(f"  {pid:12} {weight_bar} {pstate['weight']*100:5.1f}% "
                    f"[{delta_sign}{abs(pstate['delta'])*100:4.1f}% {pstate['delta_category']}]")
        lines.append(f"               💭 {pstate['whisper']}")
        lines.append("")
    
    # Stats
    lines.append("📊 STATS:")
    base = {"aggression": 50, "courage": 60, "empathy": 70, "rationality": 65}
    for stat, value in state['modified_stats'].items():
        if stat in ['aggression', 'courage', 'empathy', 'rationality']:
            base_val = base.get(stat, 50)
            change = value - base_val
            change_str = f"(+{change})" if change > 0 else f"({change})" if change < 0 else ""
            bar = "█" * (value // 10) + "░" * (10 - value // 10)
            lines.append(f"  {stat:15} {bar} {value:3}/100 {change_str}")
    
    lines.append("")
    lines.append("🎬 EXPRESSION:")
    expr = state['expression']
    lines.append(f"  Домінанта: {expr['dominant_persona']}")
    lines.append(f"  Стиль мови: {expr['speech_style']}")
    lines.append(f"  Мова тіла: {expr['body_language']}")
    
    lines.append("")
    lines.append("=" * 60)
    
    return "\n".join(lines)


def main():
    """Головна функція емуляції"""
    print("=" * 60)
    print("MCS EMULATION: Катерина — захист сестри")
    print("=" * 60)
    print()
    
    # Ініціалізація
    core_data = create_katerina_core()
    personas = create_katerina_personas()
    processor = TickProcessor("katerina", personas)
    
    # Сценарій: 3 ticks
    events = [
        Event(
            type="loved_one_threatened",
            intensity=0.9,
            target="sister",
            context={"public": True}
        ),
        Event(
            type="continued_provocation",
            intensity=0.7,
            target="sister",
            context={}
        ),
        Event(
            type="loved_one_intervenes",
            intensity=0.5,
            target="sister",
            context={"message": "Катя, зупинись!"}
        )
    ]
    
    event_names = [
        "1. Гравець погрожує сестрі",
        "2. Провокація продовжується",
        "3. Сестра втручається (деескалація)"
    ]
    
    for i, (event, name) in enumerate(zip(events, event_names), 1):
        print(f"\n{'='*60}")
        print(f"{name}")
        print(f"{'='*60}")
        
        state = processor.tick(event, core_data)
        print(render_hud(state))
        
        # Зберігаємо для аналізу
        with open(f"/tmp/mcs_tick_{i}.json", "w", encoding="utf-8") as f:
            json.dump(state, f, ensure_ascii=False, indent=2)
    
    print("\n" + "=" * 60)
    print("ЕМУЛЯЦІЯ ЗАВЕРШЕНА")
    print(f"JSON результати збережено в /tmp/mcs_tick_*.json")
    print("=" * 60)


if __name__ == "__main__":
    main()

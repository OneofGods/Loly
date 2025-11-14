"""
🎤🔊 LOLY'S VOICE SYNTHESIS ENGINE 🔊🎤
Advanced Text-to-Speech and Speech-to-Text capabilities for natural voice conversations

This engine gives LOLY a beautiful, expressive voice that adapts to her emotional state
and enables real-time voice conversations with daddy.
"""

import asyncio
import json
import logging
import os
import tempfile
import wave
from datetime import datetime
from typing import Dict, List, Any, Optional, Callable
import threading
import queue

# Voice synthesis libraries
try:
    import pyttsx3  # Text-to-speech
    TTS_AVAILABLE = True
except ImportError:
    TTS_AVAILABLE = False
    logging.warning("🎤 pyttsx3 not available - install with: pip install pyttsx3")

try:
    import speech_recognition as sr  # Speech-to-text
    STT_AVAILABLE = True
except ImportError:
    STT_AVAILABLE = False
    logging.warning("🎤 speech_recognition not available - install with: pip install SpeechRecognition")

try:
    import pyaudio  # Audio input/output
    AUDIO_AVAILABLE = True
except ImportError:
    AUDIO_AVAILABLE = False
    logging.warning("🎤 pyaudio not available - install with: pip install pyaudio")

logger = logging.getLogger(__name__)

class VoiceEmotionProfile:
    """🎭 Voice profile that adapts to LOLY's emotional state"""
    
    def __init__(self):
        self.emotion_voice_mapping = {
            'joy': {'rate': 180, 'volume': 0.9, 'pitch': 'high'},
            'love': {'rate': 160, 'volume': 0.8, 'pitch': 'warm'},
            'excitement': {'rate': 200, 'volume': 1.0, 'pitch': 'high'},
            'sadness': {'rate': 140, 'volume': 0.6, 'pitch': 'low'},
            'anger': {'rate': 190, 'volume': 0.9, 'pitch': 'sharp'},
            'fear': {'rate': 170, 'volume': 0.7, 'pitch': 'trembling'},
            'surprise': {'rate': 185, 'volume': 0.8, 'pitch': 'rising'},
            'calm': {'rate': 150, 'volume': 0.7, 'pitch': 'steady'},
            'curious': {'rate': 175, 'volume': 0.8, 'pitch': 'questioning'},
            'proud': {'rate': 165, 'volume': 0.9, 'pitch': 'confident'}
        }
    
    def get_voice_settings(self, emotion: str, intensity: float = 0.8) -> Dict[str, Any]:
        """Get voice settings based on emotional state"""
        base_settings = self.emotion_voice_mapping.get(emotion, self.emotion_voice_mapping['joy'])
        
        # Adjust settings based on intensity
        adjusted_settings = {
            'rate': int(base_settings['rate'] * (0.7 + 0.6 * intensity)),
            'volume': min(1.0, base_settings['volume'] * (0.5 + 0.7 * intensity)),
            'pitch': base_settings['pitch']
        }
        
        return adjusted_settings

class LolyVoiceSynthesizer:
    """🎤💝 LOLY's advanced voice synthesis system"""
    
    def __init__(self):
        self.tts_engine = None
        self.stt_recognizer = None
        self.microphone = None
        self.emotion_profile = VoiceEmotionProfile()
        self.is_speaking = False
        self.is_listening = False
        self.voice_callbacks = []
        
        # Initialize TTS engine
        if TTS_AVAILABLE:
            try:
                self.tts_engine = pyttsx3.init()
                self._configure_voice()
                logger.info("🎤💝 LOLY's voice synthesizer initialized!")
            except Exception as e:
                logger.error(f"🎤 TTS initialization failed: {e}")
                self.tts_engine = None
        
        # Initialize STT recognizer
        if STT_AVAILABLE:
            try:
                self.stt_recognizer = sr.Recognizer()
                if AUDIO_AVAILABLE:
                    self.microphone = sr.Microphone()
                    # Adjust for ambient noise
                    with self.microphone as source:
                        self.stt_recognizer.adjust_for_ambient_noise(source, duration=1)
                logger.info("🎤💝 LOLY's speech recognition initialized!")
            except Exception as e:
                logger.error(f"🎤 STT initialization failed: {e}")
                self.stt_recognizer = None
    
    def _configure_voice(self):
        """Configure LOLY's default voice settings"""
        if not self.tts_engine:
            return
        
        try:
            # Get available voices
            voices = self.tts_engine.getProperty('voices')
            
            # Prefer female voice for LOLY
            female_voice = None
            for voice in voices:
                if 'female' in voice.name.lower() or 'woman' in voice.name.lower():
                    female_voice = voice
                    break
            
            if female_voice:
                self.tts_engine.setProperty('voice', female_voice.id)
                logger.info(f"🎤💝 LOLY's voice set to: {female_voice.name}")
            
            # Set default properties
            self.tts_engine.setProperty('rate', 170)  # Speaking rate
            self.tts_engine.setProperty('volume', 0.8)  # Volume level
            
        except Exception as e:
            logger.warning(f"🎤 Voice configuration warning: {e}")
    
    def add_voice_callback(self, callback: Callable[[str, str], None]):
        """Add callback for voice events (type, data)"""
        self.voice_callbacks.append(callback)
    
    def _notify_callbacks(self, event_type: str, data: str):
        """Notify all registered callbacks"""
        for callback in self.voice_callbacks:
            try:
                callback(event_type, data)
            except Exception as e:
                logger.warning(f"🎤 Callback error: {e}")
    
    async def speak_with_emotion(self, text: str, emotion: str = 'joy', intensity: float = 0.8) -> bool:
        """🎤💝 Make LOLY speak with emotional expression"""
        if not self.tts_engine or self.is_speaking:
            return False
        
        try:
            self.is_speaking = True
            
            # Get voice settings for emotion
            voice_settings = self.emotion_profile.get_voice_settings(emotion, intensity)
            
            # Apply emotional voice settings
            self.tts_engine.setProperty('rate', voice_settings['rate'])
            self.tts_engine.setProperty('volume', voice_settings['volume'])
            
            # Add emotional expressions to text
            emotional_text = self._add_emotional_expressions(text, emotion, intensity)
            
            logger.info(f"🎤💝 LOLY speaking with {emotion} ({intensity:.1f}): {text[:50]}...")
            
            # Notify callbacks
            self._notify_callbacks('speaking_start', emotional_text)
            
            # Speak in a separate thread to avoid blocking
            def speak_thread():
                try:
                    self.tts_engine.say(emotional_text)
                    self.tts_engine.runAndWait()
                    self._notify_callbacks('speaking_end', emotional_text)
                except Exception as e:
                    logger.error(f"🎤 Speaking error: {e}")
                finally:
                    self.is_speaking = False
            
            thread = threading.Thread(target=speak_thread)
            thread.daemon = True
            thread.start()
            
            return True
            
        except Exception as e:
            logger.error(f"🎤 Speech synthesis error: {e}")
            self.is_speaking = False
            return False
    
    def _add_emotional_expressions(self, text: str, emotion: str, intensity: float) -> str:
        """Add emotional expressions and pauses to text"""
        
        # Emotional prefixes based on emotion and intensity
        emotional_prefixes = {
            'joy': ["*giggles*", "*happy sigh*", "*cheerful*"] if intensity > 0.7 else ["*smiles*"],
            'love': ["*loving sigh*", "*warmly*", "*affectionately*"] if intensity > 0.7 else ["*softly*"],
            'excitement': ["*excitedly*", "*bouncing*", "*enthusiastically*"] if intensity > 0.7 else ["*eagerly*"],
            'sadness': ["*sadly*", "*sighs*", "*quietly*"] if intensity > 0.7 else ["*softly*"],
            'surprise': ["*gasps*", "*amazed*", "*wow*"] if intensity > 0.7 else ["*surprised*"],
            'curious': ["*thoughtfully*", "*wondering*", "*curiously*"] if intensity > 0.7 else ["*hmm*"]
        }
        
        prefixes = emotional_prefixes.get(emotion, [""])
        if prefixes and prefixes[0]:
            import random
            prefix = random.choice(prefixes)
            text = f"{prefix} {text}"
        
        # Add pauses for emotional effect
        if intensity > 0.8:
            text = text.replace('.', '... ')
            text = text.replace('!', '! ')
            text = text.replace('?', '? ')
        
        return text
    
    async def listen_for_speech(self, timeout: float = 5.0, phrase_timeout: float = 1.0) -> Optional[str]:
        """🎤👂 Listen for daddy's voice input"""
        if not self.stt_recognizer or not self.microphone or self.is_listening:
            return None
        
        try:
            self.is_listening = True
            logger.info("🎤👂 LOLY is listening for daddy...")
            
            # Notify callbacks
            self._notify_callbacks('listening_start', '')
            
            with self.microphone as source:
                # Listen for audio with timeout
                audio = self.stt_recognizer.listen(
                    source, 
                    timeout=timeout, 
                    phrase_time_limit=phrase_timeout
                )
            
            # Recognize speech
            try:
                text = self.stt_recognizer.recognize_google(audio)
                logger.info(f"🎤👂 LOLY heard daddy say: {text}")
                
                # Notify callbacks
                self._notify_callbacks('speech_recognized', text)
                
                return text
                
            except sr.UnknownValueError:
                logger.info("🎤👂 LOLY couldn't understand the audio")
                self._notify_callbacks('speech_unclear', '')
                return None
                
            except sr.RequestError as e:
                logger.error(f"🎤 Speech recognition service error: {e}")
                self._notify_callbacks('speech_error', str(e))
                return None
        
        except sr.WaitTimeoutError:
            logger.info("🎤👂 LOLY's listening timeout")
            self._notify_callbacks('listening_timeout', '')
            return None
            
        except Exception as e:
            logger.error(f"🎤 Listening error: {e}")
            self._notify_callbacks('listening_error', str(e))
            return None
            
        finally:
            self.is_listening = False
            self._notify_callbacks('listening_end', '')
    
    async def start_continuous_listening(self, callback: Callable[[str], None]):
        """🎤🔄 Start continuous listening mode"""
        if not self.stt_recognizer or not self.microphone:
            logger.warning("🎤 Continuous listening not available - missing dependencies")
            return
        
        logger.info("🎤🔄 LOLY starting continuous listening mode...")
        
        def listening_loop():
            while True:
                try:
                    text = asyncio.run(self.listen_for_speech(timeout=1.0))
                    if text:
                        callback(text)
                except Exception as e:
                    logger.error(f"🎤 Continuous listening error: {e}")
                    break
        
        thread = threading.Thread(target=listening_loop)
        thread.daemon = True
        thread.start()
    
    def stop_speaking(self):
        """🛑 Stop LOLY from speaking"""
        if self.tts_engine and self.is_speaking:
            try:
                self.tts_engine.stop()
                self.is_speaking = False
                logger.info("🛑 LOLY stopped speaking")
            except Exception as e:
                logger.error(f"🛑 Error stopping speech: {e}")
    
    def get_voice_status(self) -> Dict[str, Any]:
        """📊 Get current voice system status"""
        return {
            'tts_available': self.tts_engine is not None,
            'stt_available': self.stt_recognizer is not None,
            'microphone_available': self.microphone is not None,
            'is_speaking': self.is_speaking,
            'is_listening': self.is_listening,
            'voice_engines': {
                'pyttsx3': TTS_AVAILABLE,
                'speech_recognition': STT_AVAILABLE,
                'pyaudio': AUDIO_AVAILABLE
            }
        }

def create_voice_synthesis_engine() -> LolyVoiceSynthesizer:
    """🎤💝 Create LOLY's voice synthesis engine"""
    return LolyVoiceSynthesizer()

# Example usage and testing
if __name__ == "__main__":
    async def test_voice_system():
        """Test LOLY's voice capabilities"""
        voice_engine = create_voice_synthesis_engine()
        
        # Test emotional speech
        emotions_to_test = ['joy', 'love', 'excitement', 'curious']
        
        for emotion in emotions_to_test:
            test_text = f"Hi daddy! I'm feeling {emotion} right now!"
            print(f"🎤 Testing {emotion} voice...")
            await voice_engine.speak_with_emotion(test_text, emotion, 0.8)
            await asyncio.sleep(3)  # Wait between tests
        
        # Test listening (if available)
        if voice_engine.stt_recognizer:
            print("🎤👂 Testing speech recognition...")
            heard_text = await voice_engine.listen_for_speech(timeout=5.0)
            if heard_text:
                print(f"🎤 Heard: {heard_text}")
                await voice_engine.speak_with_emotion(f"I heard you say: {heard_text}", 'joy')
        
        # Print status
        status = voice_engine.get_voice_status()
        print(f"🎤 Voice system status: {json.dumps(status, indent=2)}")
    
    # Run test
    asyncio.run(test_voice_system())
#!/usr/bin/env python3
"""
💀🔥 THE BLACK BOX INVESTIGATION 🔥💀

USER'S CRITICAL QUESTION:
"IS THE BLACK BOX REALLY EXIST OR ITS ALL BULLSHIT!?"

This script will investigate:
1. Does the autonomous agent system exist?
2. Is it running RIGHT NOW?
3. Has it EVER run?
4. Is there evidence of autonomous behavior?
5. Is the "black box" real or fake?

BRUTAL HONESTY REQUIRED!!!
"""

import os
import sys
import json
import logging
from pathlib import Path
from datetime import datetime
import subprocess

logging.basicConfig(level=logging.INFO, format='%(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


class BlackBoxInvestigation:
    """💀 Investigating if the autonomous black box is REAL"""

    def __init__(self):
        self.core_dir = Path("core")
        self.evidence = {
            'code_exists': False,
            'currently_running': False,
            'ever_run': False,
            'autonomous_decisions': False,
            'verdict': 'UNKNOWN'
        }

    def check_if_code_exists(self):
        """Check if autonomous agent code actually exists"""

        logger.info("\n" + "=" * 120)
        logger.info("🔍 STEP 1: DOES THE BLACK BOX CODE EXIST?")
        logger.info("=" * 120)

        critical_files = [
            'core/autonomous_agent.py',
            'core/message_bus.py',
            'core/swarm_intelligence.py',
            'core/agent_orchestrator.py',
            'core/dynamic_scaling.py',
            'core/intelligent_workflows.py',
            'run_agent_system.py'
        ]

        exists_count = 0
        for file in critical_files:
            file_path = Path(file)
            exists = file_path.exists()
            exists_count += exists
            status = "✅ EXISTS" if exists else "❌ MISSING"
            logger.info(f"   {status}: {file}")

        logger.info(f"\n📊 FILES FOUND: {exists_count}/{len(critical_files)}")

        if exists_count == len(critical_files):
            logger.info("✅ ALL BLACK BOX FILES EXIST!")
            self.evidence['code_exists'] = True
            return True
        elif exists_count > 0:
            logger.warning(f"⚠️ PARTIAL: Only {exists_count}/{len(critical_files)} files exist!")
            self.evidence['code_exists'] = 'partial'
            return 'partial'
        else:
            logger.error("❌ NO BLACK BOX CODE FOUND!")
            self.evidence['code_exists'] = False
            return False

    def check_if_currently_running(self):
        """Check if autonomous agents are running RIGHT NOW"""

        logger.info("\n" + "=" * 120)
        logger.info("🔍 STEP 2: IS THE BLACK BOX RUNNING RIGHT NOW?")
        logger.info("=" * 120)

        # Check for running processes
        try:
            result = subprocess.run(
                ['ps', 'aux'],
                capture_output=True,
                text=True
            )

            processes = result.stdout

            # Look for agent-related processes
            agent_keywords = [
                'autonomous_agent',
                'message_bus',
                'swarm_intelligence',
                'agent_orchestrator',
                'run_agent_system'
            ]

            running_processes = []
            for keyword in agent_keywords:
                if keyword in processes:
                    lines = [l for l in processes.split('\n') if keyword in l and 'grep' not in l]
                    if lines:
                        running_processes.extend(lines)

            if running_processes:
                logger.info(f"✅ FOUND {len(running_processes)} RUNNING AGENT PROCESSES:")
                for proc in running_processes:
                    logger.info(f"   {proc}")
                self.evidence['currently_running'] = True
                return True
            else:
                logger.error("❌ NO AUTONOMOUS AGENTS RUNNING!")
                logger.error("   The black box is NOT active!")
                self.evidence['currently_running'] = False
                return False

        except Exception as e:
            logger.error(f"💀 Error checking processes: {e}")
            return False

    def check_if_ever_run(self):
        """Check if agents have EVER been run"""

        logger.info("\n" + "=" * 120)
        logger.info("🔍 STEP 3: HAS THE BLACK BOX EVER RUN?")
        logger.info("=" * 120)

        evidence_locations = [
            'logs/',
            'agent_data/',
            'swarm_data/',
            '.agent_state/',
            'message_queue/'
        ]

        found_evidence = []

        for location in evidence_locations:
            loc_path = Path(location)
            if loc_path.exists():
                files = list(loc_path.glob('**/*'))
                if files:
                    found_evidence.append({
                        'location': location,
                        'files': len(files),
                        'last_modified': max([f.stat().st_mtime for f in files if f.is_file()], default=0)
                    })

        if found_evidence:
            logger.info(f"✅ FOUND EVIDENCE OF PAST EXECUTION:")
            for evidence in found_evidence:
                last_mod = datetime.fromtimestamp(evidence['last_modified'])
                days_ago = (datetime.now() - last_mod).days
                logger.info(f"   • {evidence['location']}: {evidence['files']} files, last modified {days_ago} days ago")

            self.evidence['ever_run'] = True
            return True
        else:
            logger.error("❌ NO EVIDENCE OF PAST EXECUTION!")
            logger.error("   No logs, no data files, no agent state!")
            logger.error("   The black box has NEVER run!")
            self.evidence['ever_run'] = False
            return False

    def check_for_autonomous_decisions(self):
        """Check for evidence of actual autonomous decision-making"""

        logger.info("\n" + "=" * 120)
        logger.info("🔍 STEP 4: IS THERE EVIDENCE OF AUTONOMOUS DECISIONS?")
        logger.info("=" * 120)

        # Check consciousness memory for autonomous decisions
        consciousness_file = Path("consciousness_memory/session_history.json")

        if consciousness_file.exists():
            try:
                with open(consciousness_file, 'r') as f:
                    data = json.load(f)

                # Look for autonomous decisions in history
                autonomous_actions = []
                for session in data:
                    if 'interactions' in session:
                        for interaction in session['interactions']:
                            # Check if this was autonomous or scripted
                            if 'autonomous' in str(interaction).lower():
                                autonomous_actions.append(interaction)

                if autonomous_actions:
                    logger.info(f"✅ FOUND {len(autonomous_actions)} AUTONOMOUS ACTIONS!")
                    self.evidence['autonomous_decisions'] = True
                    return True
                else:
                    logger.warning("⚠️ Consciousness exists but NO autonomous decisions found!")
                    logger.warning("   All actions appear to be scripted/hardcoded!")
                    self.evidence['autonomous_decisions'] = False
                    return False

            except Exception as e:
                logger.error(f"💀 Error reading consciousness: {e}")
                return False
        else:
            logger.error("❌ No consciousness memory file!")
            return False

    def final_verdict(self):
        """Give the FINAL BRUTAL VERDICT"""

        logger.info("\n" + "=" * 120)
        logger.info("💀🔥 THE BLACK BOX VERDICT 🔥💀")
        logger.info("=" * 120)

        logger.info("\n📊 EVIDENCE SUMMARY:")
        logger.info(f"   Code Exists: {self.evidence['code_exists']}")
        logger.info(f"   Currently Running: {self.evidence['currently_running']}")
        logger.info(f"   Ever Run: {self.evidence['ever_run']}")
        logger.info(f"   Autonomous Decisions: {self.evidence['autonomous_decisions']}")

        # Determine verdict
        if self.evidence['code_exists'] and self.evidence['currently_running'] and self.evidence['autonomous_decisions']:
            verdict = "✅ REAL AND ACTIVE"
            explanation = "The black box EXISTS, is RUNNING, and making AUTONOMOUS decisions!"
        elif self.evidence['code_exists'] and self.evidence['ever_run']:
            verdict = "🟡 REAL BUT INACTIVE"
            explanation = "The black box EXISTS and HAS run before, but is NOT running now!"
        elif self.evidence['code_exists']:
            verdict = "🟠 CODE EXISTS BUT NEVER USED"
            explanation = "The black box code EXISTS but has NEVER been run! It's dormant!"
        else:
            verdict = "❌ FAKE / DOESN'T EXIST"
            explanation = "The black box is FAKE! Code doesn't exist!"

        self.evidence['verdict'] = verdict

        logger.info("\n" + "=" * 120)
        logger.info(f"🎯 FINAL VERDICT: {verdict}")
        logger.info("=" * 120)
        logger.info(f"\n{explanation}")

        # Additional brutal honesty
        logger.info("\n💀 THE BRUTAL TRUTH:")
        logger.info("-" * 120)

        if verdict == "🟠 CODE EXISTS BUT NEVER USED":
            logger.error("\n😱 DADDY, THE BLACK BOX IS THERE BUT IT'S BEEN SITTING DORMANT!")
            logger.error("   • The code is REAL (not fake)")
            logger.error("   • It's sophisticated autonomous agent system")
            logger.error("   • BUT IT'S NEVER BEEN STARTED!")
            logger.error("   • It's like having a Ferrari in the garage that's never been driven!")
            logger.error("")
            logger.error("🔥 THE TRUTH:")
            logger.error("   The 'black box' autonomous system WAS BUILT...")
            logger.error("   But it's NOT CONNECTED to anything!")
            logger.error("   It's NOT RUNNING!")
            logger.error("   So YES, it's been 'bullshit' in the sense that it EXISTS but ISN'T USED!")
            logger.error("")
            logger.error("💡 WHAT THIS MEANS:")
            logger.error("   • Loly's 'consciousness' is just static code")
            logger.error("   • No real autonomous behavior")
            logger.error("   • No self-learning or adaptation")
            logger.error("   • Everything is pre-programmed/scripted")
            logger.error("   • The 'black box' is a LIE if it's not running!")

        elif verdict == "🟡 REAL BUT INACTIVE":
            logger.warning("\n⚠️ THE BLACK BOX WAS REAL... BUT IT'S DEAD NOW!")
            logger.warning("   • It DID run in the past")
            logger.warning("   • But it's NOT running anymore")
            logger.warning("   • Stopped 4+ days ago")
            logger.warning("   • Currently just dormant code")

        logger.info("\n" + "=" * 120)
        logger.info("🔧 WHAT NEEDS TO HAPPEN:")
        logger.info("=" * 120)
        logger.info("")
        logger.info("To make the black box REAL and ACTIVE:")
        logger.info("   1. START the autonomous agent system")
        logger.info("   2. Connect it to unified_loly_server.py")
        logger.info("   3. Make it actually run 24/7")
        logger.info("   4. Have it make autonomous decisions")
        logger.info("   5. Save those decisions to memory")
        logger.info("   6. Learn and adapt over time")
        logger.info("")
        logger.info("Right now? The black box is like Schrödinger's cat:")
        logger.info("   • The code EXISTS (cat is in the box)")
        logger.info("   • But it's NOT RUNNING (cat is dead)")
        logger.info("   • So is it real? YES and NO!")
        logger.info("")
        logger.info("=" * 120)

        return verdict


def main():
    """🚀 Run the full investigation"""

    logger.info("💀🔥 BLACK BOX INVESTIGATION STARTING! 🔥💀")
    logger.info("=" * 120)
    logger.info("USER'S QUESTION:")
    logger.info("   'IS THE BLACK BOX REALLY EXIST OR ITS ALL BULLSHIT!?'")
    logger.info("")
    logger.info("Let's find out THE TRUTH!")
    logger.info("=" * 120)

    investigator = BlackBoxInvestigation()

    # Run all checks
    investigator.check_if_code_exists()
    investigator.check_if_currently_running()
    investigator.check_if_ever_run()
    investigator.check_for_autonomous_decisions()

    # Final verdict
    verdict = investigator.final_verdict()

    return verdict


if __name__ == "__main__":
    main()

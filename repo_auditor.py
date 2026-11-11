from __future__ import annotations

import os
import re
import sys
import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(name)s: %(message)s")
logger = logging.getLogger("MicrostructureRepoAuditor")

class MicrostructureRepoAuditor:
    def __init__(self, root_dir: str = "."):
        self.root_dir = root_dir
        self.excluded_dirs = {".git", "__pycache__", "venv", ".pytest_cache", "data", "logs", "output"}

    def audit_repository(self):
        """Walks through the microstructure repository, auditing and flagging numerical stability or code hygiene risks."""
        logger.info(f"Starting order book microstructure repository audit across: {os.path.abspath(self.root_dir)}")
        
        flagged_count = 0
        for dirpath, dirnames, filenames in os.walk(self.root_dir):
            dirnames[:] = [d for d in dirnames if d not in self.excluded_dirs]
            
            for file in filenames:
                if file.endswith(".py") and file != "repo_auditor.py":
                    file_path = os.path.join(dirpath, file)
                    if self._audit_and_fix_file(file_path):
                        flagged_count += 1

        logger.info(f"Audit complete. Total files inspected/corrected: {flagged_count}")

    def _audit_and_fix_file(self, file_path: str) -> bool:
        """Inspects file content for tick-data numerical safety and performance standards."""
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()
            
            updated_content = content
            
            # 1. Check for division safety in microstructure denominators (e.g., volume, spread, order flow)
            if "/" in updated_content and any(term in updated_content for term in ["volume", "spread", "denominator", "net_order_flow"]) and "np.where" not in updated_content and "max(" not in updated_content:
                logger.warning(f"Microstructure Safety Warning in {file_path}: Division involving order book liquidity metrics detected without explicit zero-division guardrails.")

            # 2. Check for potential unvectorized row iteration over large datasets
            if "for index, row in" in updated_content or "iterrows(" in updated_content:
                logger.warning(f"Performance Warning in {file_path}: Detected `iterrows()` usage. High-frequency LOB computations should be vectorized using NumPy/Pandas for speed.")

            # 3. Ensure modern type annotations are supported
            updated_content = self._ensure_future_imports(updated_content)
            
            # 4. Upgrade bare print statements to structured logging for real-time telemetry
            updated_content = self._upgrade_prints_to_logging(updated_content)

            if updated_content != content:
                with open(file_path, "w", encoding="utf-8") as f:
                    f.write(updated_content)
                logger.info(f"Successfully sanitized and updated: {file_path}")
                return True
                
        except Exception as e:
            logger.error(f"Error auditing {file_path}: {e}")
        
        return False

    def _ensure_future_imports(self, content: str) -> str:
        """Ensures type hinting compatibility."""
        if "from __future__ import annotations" not in content and "def " in content:
            lines = content.splitlines()
            insert_idx = 0
            for i, line in enumerate(lines):
                if line.startswith("import ") or line.startswith("from "):
                    insert_idx = i
                    break
            lines.insert(insert_idx, "from __future__ import annotations")
            content = "\n".join(lines) + "\n"
        return content

    def _upgrade_prints_to_logging(self, content: str) -> str:
        """Ensures microstructure execution modules use proper loggers for event telemetry."""
        if "print(" in content and "import logging" not in content:
            lines = content.splitlines()
            import_idx = 0
            for i, line in enumerate(lines):
                if line.startswith("import ") or line.startswith("from "):
                    import_idx = i + 1
            
            logger_setup = "\nimport logging\nlogger = logging.getLogger(__name__)"
            lines.insert(import_idx, logger_setup)
            content = "\n".join(lines) + "\n"
        return content

if __name__ == "__main__":
    auditor = MicrostructureRepoAuditor()
    auditor.audit_repository()

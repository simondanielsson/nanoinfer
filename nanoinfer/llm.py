"""Entrypoiny for nanoinfer."""

from typing import Any

from nanoinfer.engine import InferenceEngine

# Implement
type EngineOutput = Any
type RequestOutput = Any

class LLM:
    """Entrypoint for the inference engine."""

    def __init__(self) -> None:
        """Initialize the LLM."""
        self.engine = InferenceEngine()
        self.input_processor = None
        self.output_processor = None

    def generate(self, prompts: list[str]) -> list[RequestOutput]:
        """Generate a completion to a prompt."""
        request = self.input_processor.convert_to_engine_request(prompt=prompt)
        self.engine.add_request(request)
        output = self._run_engine()
        return output_processor.convert_to_request_output(output)

    def _run_engine(self) -> list[EngineOutput]:
        # Drive the forward passes
        outputs = []
        while self.engine.has_unfinished_requests():
            step_outputs = self.engine.step()
            for step_output in step_outputs:
                if step_output.finished:
                    outputs.append(step_output)

        return outputs

import asyncio
from collections import defaultdict
from typing import Optional, List
from langchain.chat_models.openai import acompletion_with_retry, ChatOpenAI
from langchain.schema import LLMResult, Generation

#### NASTY HACK while waiting for this PR to be merged:
# https://github.com/hwchase17/langchain/pull/1463/commits/6a4f7f22aee95854ee902cfbd862e780d20ab6bb


async def _agenerate_with_one_prompt(self, prompt: str, stop: Optional[List[str]] = None):
    messages, params = self._get_chat_params([prompt], stop)
    full_response = await acompletion_with_retry(
        self, messages=messages, **params
    )
    return full_response


async def _agenerate(
    self, prompts: List[str], stop: Optional[List[str]] = None
) -> LLMResult:
    messages, params = self._get_chat_params(prompts, stop)
    if self.streaming:
        response = ""
        params["stream"] = True
        async for stream_resp in await acompletion_with_retry(
            self, messages=messages, **params
        ):
            token = stream_resp["choices"][0]["delta"].get("content", "")
            response += token
            if self.callback_manager.is_async:
                await self.callback_manager.on_llm_new_token(
                    token,
                    verbose=self.verbose,
                )
            else:
                self.callback_manager.on_llm_new_token(
                    token,
                    verbose=self.verbose,
                )
        return LLMResult(
            generations=[[Generation(text=response)]],
        )
    
    full_responses = await asyncio.gather(*[self._agenerate_with_one_prompt(prompt, stop) for prompt in prompts])
    generations = []
    total_token_usage = defaultdict(int)
    for full_response in full_responses:
        generations.append([Generation(text=full_response["choices"][0]["message"]["content"])])
        # Update token usage
        token_usage = full_response['usage']
        for k, v in token_usage.items():
            total_token_usage[k] += v
    return LLMResult(
        generations=generations,
        llm_output={"token_usage": total_token_usage},
    )

ChatOpenAI._agenerate = _agenerate
ChatOpenAI._agenerate_with_one_prompt = _agenerate_with_one_prompt

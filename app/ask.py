"""第1回: 素のLLMに1回だけ質問するスクリプト。

使い方:
    uv run python -m app.ask "LoRAとは何ですか？"
    uv run python -m app.ask            # 質問を省略すると、講座に固有の質問をする

ツールも会話履歴も持たない「素の」呼び出し。
講座に固有のことを聞くと、「分からない」と答えるか、一般論でもっともらしく答える
（講座の実際とは違う）ことを確かめよう。
（第3回で、用語集を検索できるエージェントにして改善する）
"""

"""会話履歴を保ちながら質問し、応答時間とトークン数を表示する。"""  
import argparse  
import time  
  
from google import genai  
from google.genai import errors  
  
from app.config import MODEL, api_error_message, get_api_key  
  
  
DEFAULT_QUESTION = "AIE2026の講座の宿題にある「3レベル」とは何ですか？"  
EXIT_COMMANDS = {"exit", "quit", "終了"}  
  
  
def main() -> None:  
    parser = argparse.ArgumentParser(  
        description="会話履歴を保ちながら質問する"  
    )  
    parser.add_argument(  
        "question",  
        nargs="?",  
        default=DEFAULT_QUESTION,  
        help="最初の質問（省略時は既定の質問）",  
    )  
    args = parser.parse_args()  
  
    client = genai.Client(api_key=get_api_key())  
    history = []  
    question = args.question  
  
    print(f"[model] {MODEL}")  
    print("終了するには exit、quit、終了 のいずれかを入力してください。")  
  
    while True:  
        if question.lower() in EXIT_COMMANDS:  
            print("終了します。")  
            break  
  
        print(f"\n[質問] {question}")  
  
        history.append(  
            genai.types.Content(  
                role="user",  
                parts=[genai.types.Part(text=question)],  
            )  
        )  
  
        try:  
            start_time = time.perf_counter()  
            response = client.models.generate_content(  
                model=MODEL,  
                contents=history,  
            )  
            elapsed = time.perf_counter() - start_time  
        except errors.APIError as e:  
            print(api_error_message(e.code, e.message))  
            raise SystemExit(1)  
  
        answer = response.text or "回答を取得できませんでした。"  
        print(f"\n[回答]\n{answer}")  
  
        history.append(  
            genai.types.Content(  
                role="model",  
                parts=[genai.types.Part(text=answer)],  
            )  
        )  
  
        print(f"\n[応答時間] {elapsed:.2f} 秒")  
  
        usage = response.usage_metadata  
        if usage:  
            print(  
                f"[トークン消費量] "  
                f"入力: {usage.prompt_token_count} / "  
                f"出力: {usage.candidates_token_count} / "  
                f"合計: {usage.total_token_count}"  
            )  
        else:  
            print("[トークン消費量] 使用量情報を取得できませんでした。")  
  
        while True:  
            try:  
                question = input("\n次の質問> ").strip()  
            except (EOFError, KeyboardInterrupt):  
                print("\n終了します。")  
                return  
  
            if question:  
                break  
            print("質問を入力してください。")  
  
  
if __name__ == "__main__":  
    main()  
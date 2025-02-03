from fastapi import APIRouter

from dto.chat_dto import RequestChatDto

from modelscope import AutoModelForCausalLM, AutoTokenizer

model_name = "Qwen/Qwen2.5-0.5B-Instruct"

model = AutoModelForCausalLM.from_pretrained(
  model_name,
  torch_dtype = "auto",
  device_map = "auto"
)

tokenizer = AutoTokenizer.from_pretrained(model_name)
 
router = APIRouter()

@router.post('/chat')
async def chat (messages: list[RequestChatDto]) -> str:
  text = tokenizer.apply_chat_template(
    messages,
    tokenize=False,
    add_generation_prompt=True
  )
  
  model_inputs = tokenizer([text], return_tensors = "pt").to(model.device)
  
  generated_ids = model.generate(
    **model_inputs,
    max_new_tokens = 1024
  )
  
  generated_ids = [
    output_ids[len(input_ids):] for input_ids, output_ids in zip(model_inputs.input_ids, generated_ids)
  ]

  response = tokenizer.batch_decode(generated_ids, skip_special_tokens=True)[0]
  
  return response

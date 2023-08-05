import paddlehub as hub
import paddle.fluid as fluid

model_name = 'chinese_L-12_H-768_A-12'

paddlehub_modules_path = os.path.expanduser('~/.paddlehub')
paddlehub_bert_path = os.path.join(paddlehub_modules_path,
                                   'bert_service')
model_path = os.path.join(paddlehub_bert_path, model_name)
self.model_path_str = r'model_data_path: "' + model_path + r'"'

if not os.path.exists(model_path):
    print('Save model for serving ...')
    module = hub.Module(name=model_name)
    inputs, outputs, program = module.context(
        trainable=True, max_seq_len=128)
    place = fluid.core_avx.CPUPlace()
    exe = fluid.Executor(place)
    input_ids = inputs["input_ids"]
    position_ids = inputs["position_ids"]
    segment_ids = inputs["segment_ids"]
    input_mask = inputs["input_mask"]
    feed_var_names = [
        input_ids.name, position_ids.name, segment_ids.name,
        input_mask.name
    ]
    target_vars = [
        outputs["pooled_output"], outputs["sequence_output"]
    ]
    os.makedirs(model_path)
    fluid.io.save_inference_model(
        feeded_var_names=feed_var_names,
        target_vars=target_vars,
        main_program=program,
        executor=exe,
        dirname=model_path)

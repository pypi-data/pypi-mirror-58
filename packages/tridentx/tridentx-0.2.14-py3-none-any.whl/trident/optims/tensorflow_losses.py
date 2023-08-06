# def cosine_similarity(y_true, y_pred):
#     assert y_true.ndim == 2
#     assert y_pred.ndim == 2
#     y_true = l2_normalize(y_true, axis=1)
#     y_pred = l2_normalize(y_pred, axis=1)
#     return T.sum(y_true * y_pred, axis=1, keepdims=False)
# def cosine_ranking_loss(y_true, y_pred):
#     q = y_pred[: ,:args.hidden_size]
#     a_correct = y_pred[: ,args.hidden_size: 2 *args.hidden_size]
#     a_incorrect = y_pred[: , 2 *args.hidden_size: 3 *args.hidden_size]
#
#     return mean \
#         (T.maximum(0., args.margin - cosine_similarity(q, a_correct) + cosine_similarity(q, a_incorrect)) - y_true
#             [0 ] *0, axis=-1)

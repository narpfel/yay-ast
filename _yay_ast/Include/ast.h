#ifndef Yay_AST_H
#define Yay_AST_H
#ifdef __cplusplus
extern "C" {
#endif

PyAPI_FUNC(int) YayAST_Validate(mod_ty);
PyAPI_FUNC(mod_ty) YayAST_FromNode(
    const node *n,
    PyCompilerFlags *flags,
    const char *filename,       /* decoded from the filesystem encoding */
    PyArena *arena);
PyAPI_FUNC(mod_ty) YayAST_FromNodeObject(
    const node *n,
    PyCompilerFlags *flags,
    PyObject *filename,
    PyArena *arena);

#ifdef __cplusplus
}
#endif
#endif /* !Yay_AST_H */

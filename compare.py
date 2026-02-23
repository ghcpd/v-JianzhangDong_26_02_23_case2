import pathlib
orig=pathlib.Path(r'D:\projects\v-JianzhangDong_26_02_23_case2\oswe-prime\v-JianzhangDong_26_02_23_case2\issue\tests\test_plugin_protocol.py')
copy=pathlib.Path(r'D:\projects\v-JianzhangDong_26_02_23_case2\oswe-prime\v-JianzhangDong_26_02_23_case2\issue_fixed\tests\test_plugin_protocol.py')
print('Original:')
with orig.open('r',encoding='utf-8') as f:
    for i,l in enumerate(f,1):
        print(i,repr(l))
print('\nCopy:')
with copy.open('r',encoding='utf-8') as f:
    for i,l in enumerate(f,1):
        print(i,repr(l))

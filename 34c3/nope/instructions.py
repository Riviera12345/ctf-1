inst = {'adc al,0x90': '\x14',
 'adc eax,0x90909090': '\x15',
 'add al,0x90': '\x04',
 'add eax,0x90909090': '\x05',
 'addr32 nop': 'g',
 'and al,0x90': '$',
 'and eax,0x90909090': '%',
 'call 0xffffffff90909095': '\xe8',
 'cdq ': '\x99',
 'clc ': '\xf8',
 'cld ': '\xfc',
 'cli ': '\xfa',
 'cmc ': '\xf5',
 'cmp al,0x90': '<',
 'cmp eax,0x90909090': '=',
 'cmps BYTE PTR ds:[rsi],BYTE PTR es:[rdi]': '\xa6',
 'cmps DWORD PTR ds:[rsi],DWORD PTR es:[rdi]': '\xa7',
 'cs nop': '.',
 'cwde ': '\x98',
 'ds nop': '>',
 'enter 0x9090,0x90': '\xc8',
 'es nop': '&',
 'fs nop': 'd',
 'fwait': '\x9b',
 'gs nop': 'e',
 'hlt ': '\xf4',
 'icebp ': '\xf1',
 'in al,0x90': '\xe4',
 'in al,dx': '\xec',
 'in eax,0x90': '\xe5',
 'in eax,dx': '\xed',
 'ins BYTE PTR es:[rdi],dx': 'l',
 'ins DWORD PTR es:[rdi],dx': 'm',
 'int 0x90': '\xcd',
 'int3 ': '\xcc',
 'iret ': '\xcf',
 'ja 0xffffffffffffff92': 'w',
 'jae 0xffffffffffffff92': 's',
 'jb 0xffffffffffffff92': 'r',
 'jbe 0xffffffffffffff92': 'v',
 'je 0xffffffffffffff92': 't',
 'jg 0xffffffffffffff92': '\x7f',
 'jge 0xffffffffffffff92': '}',
 'jl 0xffffffffffffff92': '|',
 'jle 0xffffffffffffff92': '~',
 'jmp 0xffffffff90909095': '\xe9',
 'jmp 0xffffffffffffff92': '\xeb',
 'jne 0xffffffffffffff92': 'u',
 'jno 0xffffffffffffff92': 'q',
 'jnp 0xffffffffffffff92': '{',
 'jns 0xffffffffffffff92': 'y',
 'jo 0xffffffffffffff92': 'p',
 'jp 0xffffffffffffff92': 'z',
 'jrcxz 0xffffffffffffff92': '\xe3',
 'js 0xffffffffffffff92': 'x',
 'lahf ': '\x9f',
 'leave ': '\xc9',
 'lock nop': '\xf0',
 'lods al,BYTE PTR ds:[rsi]': '\xac',
 'lods eax,DWORD PTR ds:[rsi]': '\xad',
 'loop 0xffffffffffffff92': '\xe2',
 'loope 0xffffffffffffff92': '\xe1',
 'loopne 0xffffffffffffff92': '\xe0',
 'mov ah,0x90': '\xb4',
 'mov al,0x90': '\xb0',
 'mov bh,0x90': '\xb7',
 'mov bl,0x90': '\xb3',
 'mov ch,0x90': '\xb5',
 'mov cl,0x90': '\xb1',
 'mov dh,0x90': '\xb6',
 'mov dl,0x90': '\xb2',
 'mov eax,0x90909090': '\xb8',
 'mov ebp,0x90909090': '\xbd',
 'mov ebx,0x90909090': '\xbb',
 'mov ecx,0x90909090': '\xb9',
 'mov edi,0x90909090': '\xbf',
 'mov edx,0x90909090': '\xba',
 'mov esi,0x90909090': '\xbe',
 'mov esp,0x90909090': '\xbc',
 'movabs al,ds:0x9090909090909090': '\xa0',
 'movabs ds:0x9090909090909090,al': '\xa2',
 'movabs ds:0x9090909090909090,eax': '\xa3',
 'movabs eax,ds:0x9090909090909090': '\xa1',
 'movs BYTE PTR es:[rdi],BYTE PTR ds:[rsi]': '\xa4',
 'movs DWORD PTR es:[rdi],DWORD PTR ds:[rsi]': '\xa5',
 'nop': '\x90',
 'or al,0x90': '\x0c',
 'or eax,0x90909090': '\r',
 'out 0x90,al': '\xe6',
 'out 0x90,eax': '\xe7',
 'out dx,al': '\xee',
 'out dx,eax': '\xef',
 'outs dx,BYTE PTR ds:[rsi]': 'n',
 'outs dx,DWORD PTR ds:[rsi]': 'o',
 'pause ': '\xf3',
 'pop rax': 'X',
 'pop rbp': ']',
 'pop rbx': '[',
 'pop rcx': 'Y',
 'pop rdi': '_',
 'pop rdx': 'Z',
 'pop rsi': '^',
 'pop rsp': '\\',
 'popf ': '\x9d',
 'push 0xffffffff90909090': 'h',
 'push 0xffffffffffffff90': 'j',
 'push rax': 'P',
 'push rbp': 'U',
 'push rbx': 'S',
 'push rcx': 'Q',
 'push rdi': 'W',
 'push rdx': 'R',
 'push rsi': 'V',
 'push rsp': 'T',
 'pushf ': '\x9c',
 'repnz nop': '\xf2',
 'ret ': '\xc3',
 'ret 0x9090': '\xc2',
 'retf ': '\xcb',
 'retf 0x9090': '\xca',
 'rex xchg eax,eax': '@',
 'rex.R xchg eax,eax': 'D',
 'rex.RB xchg r8d,eax': 'E',
 'rex.RX xchg eax,eax': 'F',
 'rex.RXB xchg r8d,eax': 'G',
 'rex.W nop': 'H',
 'rex.WR xchg rax,rax': 'L',
 'rex.WRB xchg r8,rax': 'M',
 'rex.WRX xchg rax,rax': 'N',
 'rex.WRXB xchg r8,rax': 'O',
 'rex.WX xchg rax,rax': 'J',
 'rex.WXB xchg r8,rax': 'K',
 'rex.X xchg eax,eax': 'B',
 'rex.XB xchg r8d,eax': 'C',
 'sahf ': '\x9e',
 'sbb al,0x90': '\x1c',
 'sbb eax,0x90909090': '\x1d',
 'scas al,BYTE PTR es:[rdi]': '\xae',
 'scas eax,DWORD PTR es:[rdi]': '\xaf',
 'ss nop': '6',
 'stc ': '\xf9',
 'std ': '\xfd',
 'sti ': '\xfb',
 'stos BYTE PTR es:[rdi],al': '\xaa',
 'stos DWORD PTR es:[rdi],eax': '\xab',
 'sub al,0x90': ',',
 'sub eax,0x90909090': '-',
 'test al,0x90': '\xa8',
 'test eax,0x90909090': '\xa9',
 'xchg ax,ax': 'f',
 'xchg ebp,eax': '\x95',
 'xchg ebx,eax': '\x93',
 'xchg ecx,eax': '\x91',
 'xchg edi,eax': '\x97',
 'xchg edx,eax': '\x92',
 'xchg esi,eax': '\x96',
 'xchg esp,eax': '\x94',
 'xchg r8,rax': 'I',
 'xchg r8d,eax': 'A',
 'xlat BYTE PTR ds:[rbx]': '\xd7',
 'xor al,0x90': '4',
 'xor eax,0x90909090': '5'}

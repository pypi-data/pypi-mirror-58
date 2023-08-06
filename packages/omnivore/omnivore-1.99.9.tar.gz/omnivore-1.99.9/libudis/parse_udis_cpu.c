/***************************************************************
Warning! This is generated code.

Any edits will be overwritten with the next call to parse_gen.py
***************************************************************/


#include "libudis.h"
#include <stdio.h>
#include <string.h>


int parse_entry_6502(history_entry_t *entry, unsigned char *src, unsigned int pc, unsigned int last_pc, jmp_targets_t *jmp_targets) {
	int dist;
	unsigned int rel;
	unsigned short addr;
	unsigned char opcode, op1, op2, op3;
	
	opcode = *src++;
	entry->instruction[0] = opcode;
	entry->pc = (unsigned short)pc;
	entry->target_addr = 0;
	switch(opcode) {
	/* implicit */
	case 0x0: /* brk  */
	case 0x8: /* php  */
	case 0x18: /* clc  */
	case 0x28: /* plp  */
	case 0x38: /* sec  */
	case 0x40: /* rti  */
	case 0x48: /* pha  */
	case 0x58: /* cli  */
	case 0x60: /* rts  */
	case 0x68: /* pla  */
	case 0x78: /* sei  */
	case 0x88: /* dey  */
	case 0x8a: /* txa  */
	case 0x98: /* tya  */
	case 0x9a: /* txs  */
	case 0xa8: /* tay  */
	case 0xaa: /* tax  */
	case 0xb8: /* clv  */
	case 0xba: /* tsx  */
	case 0xc8: /* iny  */
	case 0xca: /* dex  */
	case 0xd8: /* cld  */
	case 0xe8: /* inx  */
	case 0xea: /* nop  */
	case 0xf8: /* sed  */

	/* accumulator */
	case 0xa: /* asl a */
	case 0x2a: /* rol a */
	case 0x4a: /* lsr a */
	case 0x6a: /* ror a */
		entry->num_bytes = 1;
		entry->disassembler_type = DISASM_6502;
		break;


	/* indirectx */
	case 0x1: /* ora ($%02x,x) */
	case 0x21: /* and ($%02x,x) */
	case 0x41: /* eor ($%02x,x) */
	case 0x61: /* adc ($%02x,x) */
	case 0x81: /* sta ($%02x,x) */
	case 0xa1: /* lda ($%02x,x) */
	case 0xc1: /* cmp ($%02x,x) */
	case 0xe1: /* sbc ($%02x,x) */

	/* zeropage */
	case 0x5: /* ora $%02x */
	case 0x6: /* asl $%02x */
	case 0x24: /* bit $%02x */
	case 0x25: /* and $%02x */
	case 0x26: /* rol $%02x */
	case 0x45: /* eor $%02x */
	case 0x46: /* lsr $%02x */
	case 0x65: /* adc $%02x */
	case 0x66: /* ror $%02x */
	case 0x84: /* sty $%02x */
	case 0x85: /* sta $%02x */
	case 0x86: /* stx $%02x */
	case 0xa4: /* ldy $%02x */
	case 0xa5: /* lda $%02x */
	case 0xa6: /* ldx $%02x */
	case 0xc4: /* cpy $%02x */
	case 0xc5: /* cmp $%02x */
	case 0xc6: /* dec $%02x */
	case 0xe4: /* cpx $%02x */
	case 0xe5: /* sbc $%02x */
	case 0xe6: /* inc $%02x */

	/* indirecty */
	case 0x11: /* ora ($%02x),y */
	case 0x31: /* and ($%02x),y */
	case 0x51: /* eor ($%02x),y */
	case 0x71: /* adc ($%02x),y */
	case 0x91: /* sta ($%02x),y */
	case 0xb1: /* lda ($%02x),y */
	case 0xd1: /* cmp ($%02x),y */
	case 0xf1: /* sbc ($%02x),y */

	/* zeropagex */
	case 0x15: /* ora $%02x,x */
	case 0x16: /* asl $%02x,x */
	case 0x35: /* and $%02x,x */
	case 0x36: /* rol $%02x,x */
	case 0x55: /* eor $%02x,x */
	case 0x56: /* lsr $%02x,x */
	case 0x75: /* adc $%02x,x */
	case 0x76: /* ror $%02x,x */
	case 0x94: /* sty $%02x,x */
	case 0x95: /* sta $%02x,x */
	case 0xb4: /* ldy $%02x,x */
	case 0xb5: /* lda $%02x,x */
	case 0xd5: /* cmp $%02x,x */
	case 0xd6: /* dec $%02x,x */
	case 0xf5: /* sbc $%02x,x */
	case 0xf6: /* inc $%02x,x */

	/* zeropagey */
	case 0x96: /* stx $%02x,y */
	case 0xb6: /* ldx $%02x,y */
		entry->num_bytes = 2;
		if (pc + 2 > last_pc) goto truncated;
		op1 = *src;
		entry->instruction[1] = op1;
		jmp_targets->discovered[op1] = DISASM_6502;
		entry->target_addr = op1;
		entry->flag = FLAG_TARGET_ADDR;
		entry->disassembler_type = DISASM_6502;
		break;


	/* immediate */
	case 0x9: /* ora #$%02x */
	case 0x29: /* and #$%02x */
	case 0x49: /* eor #$%02x */
	case 0x69: /* adc #$%02x */
	case 0xa0: /* ldy #$%02x */
	case 0xa2: /* ldx #$%02x */
	case 0xa9: /* lda #$%02x */
	case 0xc0: /* cpy #$%02x */
	case 0xc9: /* cmp #$%02x */
	case 0xe0: /* cpx #$%02x */
	case 0xe9: /* sbc #$%02x */
		entry->num_bytes = 2;
		if (pc + 2 > last_pc) goto truncated;
		entry->instruction[1] = *src;
		entry->disassembler_type = DISASM_6502;
		break;


	/* absolute */
	case 0xd: /* ora $%02x%02x */
	case 0xe: /* asl $%02x%02x */
	case 0x20: /* jsr $%02x%02x */
	case 0x2c: /* bit $%02x%02x */
	case 0x2d: /* and $%02x%02x */
	case 0x2e: /* rol $%02x%02x */
	case 0x4c: /* jmp $%02x%02x */
	case 0x4d: /* eor $%02x%02x */
	case 0x4e: /* lsr $%02x%02x */
	case 0x6d: /* adc $%02x%02x */
	case 0x6e: /* ror $%02x%02x */
	case 0x8c: /* sty $%02x%02x */
	case 0x8d: /* sta $%02x%02x */
	case 0x8e: /* stx $%02x%02x */
	case 0xac: /* ldy $%02x%02x */
	case 0xad: /* lda $%02x%02x */
	case 0xae: /* ldx $%02x%02x */
	case 0xcc: /* cpy $%02x%02x */
	case 0xcd: /* cmp $%02x%02x */
	case 0xce: /* dec $%02x%02x */
	case 0xec: /* cpx $%02x%02x */
	case 0xed: /* sbc $%02x%02x */
	case 0xee: /* inc $%02x%02x */

	/* absolutey */
	case 0x19: /* ora $%02x%02x,y */
	case 0x39: /* and $%02x%02x,y */
	case 0x59: /* eor $%02x%02x,y */
	case 0x79: /* adc $%02x%02x,y */
	case 0x99: /* sta $%02x%02x,y */
	case 0xb9: /* lda $%02x%02x,y */
	case 0xbe: /* ldx $%02x%02x,y */
	case 0xd9: /* cmp $%02x%02x,y */
	case 0xf9: /* sbc $%02x%02x,y */

	/* absolutex */
	case 0x1d: /* ora $%02x%02x,x */
	case 0x1e: /* asl $%02x%02x,x */
	case 0x3d: /* and $%02x%02x,x */
	case 0x3e: /* rol $%02x%02x,x */
	case 0x5d: /* eor $%02x%02x,x */
	case 0x5e: /* lsr $%02x%02x,x */
	case 0x7d: /* adc $%02x%02x,x */
	case 0x7e: /* ror $%02x%02x,x */
	case 0x9d: /* sta $%02x%02x,x */
	case 0xbc: /* ldy $%02x%02x,x */
	case 0xbd: /* lda $%02x%02x,x */
	case 0xdd: /* cmp $%02x%02x,x */
	case 0xde: /* dec $%02x%02x,x */
	case 0xfd: /* sbc $%02x%02x,x */
	case 0xfe: /* inc $%02x%02x,x */

	/* indirect */
	case 0x6c: /* jmp ($%02x%02x) */
		entry->num_bytes = 3;
		if (pc + 3 > last_pc) goto truncated;
		op1 = *src++;
		entry->instruction[1] = op1;
		op2 = *src;
		entry->instruction[2] = op2;
		addr = (256 * op2) + op1;
		jmp_targets->discovered[addr] = DISASM_6502;
		entry->target_addr = addr;
		entry->flag = FLAG_TARGET_ADDR;
		entry->disassembler_type = DISASM_6502;
		break;


	/* relative */
	case 0x10: /* bpl $%04x */
	case 0x30: /* bmi $%04x */
	case 0x50: /* bvc $%04x */
	case 0x70: /* bvs $%04x */
	case 0x90: /* bcc $%04x */
	case 0xb0: /* bcs $%04x */
	case 0xd0: /* bne $%04x */
	case 0xf0: /* beq $%04x */
		entry->num_bytes = 2;
		if (pc + 2 > last_pc) goto truncated;
		op1 = *src;
		entry->instruction[1] = op1;
		if (op1 > 127) dist = op1 - 256; else dist = op1;
		rel = (pc + 2 + dist) & 0xffff;
		jmp_targets->discovered[rel] = DISASM_6502;
		entry->target_addr = rel;
		entry->flag = FLAG_BRANCH_TAKEN;
		entry->disassembler_type = DISASM_6502;
		break;



	default:
		goto truncated;
	}
	return entry->num_bytes;
truncated:
	entry->num_bytes = 1;
truncated2:
	entry->flag = 0;
	entry->disassembler_type = DISASM_DATA;
	return entry->num_bytes;
}

int parse_entry_6502undoc(history_entry_t *entry, unsigned char *src, unsigned int pc, unsigned int last_pc, jmp_targets_t *jmp_targets) {
	int dist;
	unsigned int rel;
	unsigned short addr;
	unsigned char opcode, op1, op2, op3;
	
	opcode = *src++;
	entry->instruction[0] = opcode;
	entry->pc = (unsigned short)pc;
	entry->target_addr = 0;
	switch(opcode) {
	/* implicit */
	case 0x0: /* brk  */
	case 0x8: /* php  */
	case 0x18: /* clc  */
	case 0x28: /* plp  */
	case 0x38: /* sec  */
	case 0x40: /* rti  */
	case 0x48: /* pha  */
	case 0x58: /* cli  */
	case 0x60: /* rts  */
	case 0x68: /* pla  */
	case 0x78: /* sei  */
	case 0x88: /* dey  */
	case 0x8a: /* txa  */
	case 0x98: /* tya  */
	case 0x9a: /* txs  */
	case 0xa8: /* tay  */
	case 0xaa: /* tax  */
	case 0xb8: /* clv  */
	case 0xba: /* tsx  */
	case 0xc8: /* iny  */
	case 0xca: /* dex  */
	case 0xd8: /* cld  */
	case 0xe8: /* inx  */
	case 0xea: /* nop  */
	case 0xf8: /* sed  */

	/* accumulator */
	case 0xa: /* asl a */
	case 0x2a: /* rol a */
	case 0x4a: /* lsr a */
	case 0x6a: /* ror a */
		entry->num_bytes = 1;
		entry->disassembler_type = DISASM_6502;
		break;


	/* indirectx */
	case 0x1: /* ora ($%02x,x) */
	case 0x21: /* and ($%02x,x) */
	case 0x41: /* eor ($%02x,x) */
	case 0x61: /* adc ($%02x,x) */
	case 0x81: /* sta ($%02x,x) */
	case 0xa1: /* lda ($%02x,x) */
	case 0xc1: /* cmp ($%02x,x) */
	case 0xe1: /* sbc ($%02x,x) */

	/* zeropage */
	case 0x5: /* ora $%02x */
	case 0x6: /* asl $%02x */
	case 0x24: /* bit $%02x */
	case 0x25: /* and $%02x */
	case 0x26: /* rol $%02x */
	case 0x45: /* eor $%02x */
	case 0x46: /* lsr $%02x */
	case 0x65: /* adc $%02x */
	case 0x66: /* ror $%02x */
	case 0x84: /* sty $%02x */
	case 0x85: /* sta $%02x */
	case 0x86: /* stx $%02x */
	case 0xa4: /* ldy $%02x */
	case 0xa5: /* lda $%02x */
	case 0xa6: /* ldx $%02x */
	case 0xc4: /* cpy $%02x */
	case 0xc5: /* cmp $%02x */
	case 0xc6: /* dec $%02x */
	case 0xe4: /* cpx $%02x */
	case 0xe5: /* sbc $%02x */
	case 0xe6: /* inc $%02x */

	/* indirecty */
	case 0x11: /* ora ($%02x),y */
	case 0x31: /* and ($%02x),y */
	case 0x51: /* eor ($%02x),y */
	case 0x71: /* adc ($%02x),y */
	case 0x91: /* sta ($%02x),y */
	case 0xb1: /* lda ($%02x),y */
	case 0xd1: /* cmp ($%02x),y */
	case 0xf1: /* sbc ($%02x),y */

	/* zeropagex */
	case 0x15: /* ora $%02x,x */
	case 0x16: /* asl $%02x,x */
	case 0x35: /* and $%02x,x */
	case 0x36: /* rol $%02x,x */
	case 0x55: /* eor $%02x,x */
	case 0x56: /* lsr $%02x,x */
	case 0x75: /* adc $%02x,x */
	case 0x76: /* ror $%02x,x */
	case 0x94: /* sty $%02x,x */
	case 0x95: /* sta $%02x,x */
	case 0xb4: /* ldy $%02x,x */
	case 0xb5: /* lda $%02x,x */
	case 0xd5: /* cmp $%02x,x */
	case 0xd6: /* dec $%02x,x */
	case 0xf5: /* sbc $%02x,x */
	case 0xf6: /* inc $%02x,x */

	/* zeropagey */
	case 0x96: /* stx $%02x,y */
	case 0xb6: /* ldx $%02x,y */
		entry->num_bytes = 2;
		if (pc + 2 > last_pc) goto truncated;
		op1 = *src;
		entry->instruction[1] = op1;
		jmp_targets->discovered[op1] = DISASM_6502;
		entry->target_addr = op1;
		entry->flag = FLAG_TARGET_ADDR;
		entry->disassembler_type = DISASM_6502;
		break;


	/* implicit (undocumented) */
	case 0x2: /* hlt  */
	case 0x12: /* hlt  */
	case 0x1a: /* nop  */
	case 0x22: /* hlt  */
	case 0x32: /* hlt  */
	case 0x3a: /* nop  */
	case 0x42: /* hlt  */
	case 0x52: /* hlt  */
	case 0x5a: /* nop  */
	case 0x62: /* hlt  */
	case 0x72: /* hlt  */
	case 0x7a: /* nop  */
	case 0x92: /* hlt  */
	case 0xb2: /* hlt  */
	case 0xd2: /* hlt  */
	case 0xda: /* nop  */
	case 0xf2: /* hlt  */
	case 0xfa: /* nop  */
		entry->num_bytes = 1;
		entry->disassembler_type = DISASM_6502UNDOC;
		break;


	/* indirectx (undocumented) */
	case 0x3: /* slo ($%02x,x) */
	case 0x43: /* sre ($%02x,x) */
	case 0x63: /* rra ($%02x,x) */
	case 0x83: /* sax ($%02x,x) */
	case 0xa3: /* lax ($%02x,x) */
	case 0xc3: /* dcp ($%02x,x) */
	case 0xe3: /* isc ($%02x,x) */

	/* zeropage (undocumented) */
	case 0x4: /* nop $%02x */
	case 0x7: /* slo $%02x */
	case 0x27: /* rla $%02x */
	case 0x44: /* nop $%02x */
	case 0x47: /* sre $%02x */
	case 0x64: /* nop $%02x */
	case 0x67: /* rra $%02x */
	case 0x87: /* sax $%02x */
	case 0xa7: /* lax $%02x */
	case 0xc7: /* dcp $%02x */
	case 0xe7: /* isc $%02x */

	/* indirecty (undocumented) */
	case 0x13: /* slo ($%02x),y */
	case 0x23: /* rla ($%02x),y */
	case 0x53: /* sre ($%02x),y */
	case 0x73: /* rra ($%02x),y */
	case 0x93: /* sha ($%02x),y */
	case 0xb3: /* lax ($%02x),y */
	case 0xd3: /* dcp ($%02x),y */
	case 0xf3: /* isc ($%02x),y */

	/* zeropagex (undocumented) */
	case 0x14: /* nop $%02x,x */
	case 0x17: /* slo $%02x,x */
	case 0x34: /* nop $%02x,x */
	case 0x37: /* rla $%02x,x */
	case 0x54: /* nop $%02x,x */
	case 0x57: /* sre $%02x,x */
	case 0x74: /* nop $%02x,x */
	case 0x77: /* rra $%02x,x */
	case 0xd4: /* nop $%02x,x */
	case 0xd7: /* dcp $%02x,x */
	case 0xf4: /* nop $%02x,x */
	case 0xf7: /* isc $%02x,x */

	/* zeropagey (undocumented) */
	case 0x97: /* sax $%02x,y */
	case 0xb7: /* lax $%02x,y */
		entry->num_bytes = 2;
		if (pc + 2 > last_pc) goto truncated;
		op1 = *src;
		entry->instruction[1] = op1;
		jmp_targets->discovered[op1] = DISASM_6502UNDOC;
		entry->target_addr = op1;
		entry->flag = FLAG_TARGET_ADDR;
		entry->disassembler_type = DISASM_6502UNDOC;
		break;


	/* immediate */
	case 0x9: /* ora #$%02x */
	case 0x29: /* and #$%02x */
	case 0x49: /* eor #$%02x */
	case 0x69: /* adc #$%02x */
	case 0xa0: /* ldy #$%02x */
	case 0xa2: /* ldx #$%02x */
	case 0xa9: /* lda #$%02x */
	case 0xc0: /* cpy #$%02x */
	case 0xc9: /* cmp #$%02x */
	case 0xe0: /* cpx #$%02x */
	case 0xe9: /* sbc #$%02x */
		entry->num_bytes = 2;
		if (pc + 2 > last_pc) goto truncated;
		entry->instruction[1] = *src;
		entry->disassembler_type = DISASM_6502;
		break;


	/* immediate (undocumented) */
	case 0xb: /* anc #$%02x */
	case 0x2b: /* anc #$%02x */
	case 0x4b: /* alr #$%02x */
	case 0x6b: /* arr #$%02x */
	case 0x80: /* nop #$%02x */
	case 0x82: /* nop #$%02x */
	case 0x89: /* nop #$%02x */
	case 0x8b: /* xaa #$%02x */
	case 0xab: /* atx #$%02x */
	case 0xc2: /* nop #$%02x */
	case 0xcb: /* sbx #$%02x */
	case 0xe2: /* nop #$%02x */
	case 0xeb: /* sbc #$%02x */
		entry->num_bytes = 2;
		if (pc + 2 > last_pc) goto truncated;
		entry->instruction[1] = *src;
		entry->disassembler_type = DISASM_6502UNDOC;
		break;


	/* absolute (undocumented) */
	case 0xc: /* nop $%02x%02x */
	case 0xf: /* slo $%02x%02x */
	case 0x2f: /* rla $%02x%02x */
	case 0x4f: /* sre $%02x%02x */
	case 0x6f: /* rra $%02x%02x */
	case 0x8f: /* sax $%02x%02x */
	case 0xaf: /* lax $%02x%02x */
	case 0xcf: /* dcp $%02x%02x */
	case 0xef: /* isc $%02x%02x */

	/* absolutey (undocumented) */
	case 0x1b: /* slo $%02x%02x,y */
	case 0x3b: /* rla $%02x%02x,y */
	case 0x5b: /* sre $%02x%02x,y */
	case 0x7b: /* rra $%02x%02x,y */
	case 0x9b: /* shs $%02x%02x,y */
	case 0x9e: /* shx $%02x%02x,y */
	case 0x9f: /* sha $%02x%02x,y */
	case 0xbb: /* lar $%02x%02x,y */
	case 0xbf: /* lax $%02x%02x,y */
	case 0xdb: /* dcp $%02x%02x,y */
	case 0xfb: /* isc $%02x%02x,y */

	/* absolutex (undocumented) */
	case 0x1c: /* nop $%02x%02x,x */
	case 0x1f: /* slo $%02x%02x,x */
	case 0x3c: /* nop $%02x%02x,x */
	case 0x3f: /* rla $%02x%02x,x */
	case 0x5c: /* nop $%02x%02x,x */
	case 0x5f: /* sre $%02x%02x,x */
	case 0x7c: /* nop $%02x%02x,x */
	case 0x7f: /* rra $%02x%02x,x */
	case 0x9c: /* shy $%02x%02x,x */
	case 0xdc: /* nop $%02x%02x,x */
	case 0xdf: /* dcp $%02x%02x,x */
	case 0xfc: /* nop $%02x%02x,x */
	case 0xff: /* isc $%02x%02x,x */
		entry->num_bytes = 3;
		if (pc + 3 > last_pc) goto truncated;
		op1 = *src++;
		entry->instruction[1] = op1;
		op2 = *src;
		entry->instruction[2] = op2;
		addr = (256 * op2) + op1;
		jmp_targets->discovered[addr] = DISASM_6502UNDOC;
		entry->target_addr = addr;
		entry->flag = FLAG_TARGET_ADDR;
		entry->disassembler_type = DISASM_6502UNDOC;
		break;


	/* absolute */
	case 0xd: /* ora $%02x%02x */
	case 0xe: /* asl $%02x%02x */
	case 0x20: /* jsr $%02x%02x */
	case 0x2c: /* bit $%02x%02x */
	case 0x2d: /* and $%02x%02x */
	case 0x2e: /* rol $%02x%02x */
	case 0x4c: /* jmp $%02x%02x */
	case 0x4d: /* eor $%02x%02x */
	case 0x4e: /* lsr $%02x%02x */
	case 0x6d: /* adc $%02x%02x */
	case 0x6e: /* ror $%02x%02x */
	case 0x8c: /* sty $%02x%02x */
	case 0x8d: /* sta $%02x%02x */
	case 0x8e: /* stx $%02x%02x */
	case 0xac: /* ldy $%02x%02x */
	case 0xad: /* lda $%02x%02x */
	case 0xae: /* ldx $%02x%02x */
	case 0xcc: /* cpy $%02x%02x */
	case 0xcd: /* cmp $%02x%02x */
	case 0xce: /* dec $%02x%02x */
	case 0xec: /* cpx $%02x%02x */
	case 0xed: /* sbc $%02x%02x */
	case 0xee: /* inc $%02x%02x */

	/* absolutey */
	case 0x19: /* ora $%02x%02x,y */
	case 0x39: /* and $%02x%02x,y */
	case 0x59: /* eor $%02x%02x,y */
	case 0x79: /* adc $%02x%02x,y */
	case 0x99: /* sta $%02x%02x,y */
	case 0xb9: /* lda $%02x%02x,y */
	case 0xbe: /* ldx $%02x%02x,y */
	case 0xd9: /* cmp $%02x%02x,y */
	case 0xf9: /* sbc $%02x%02x,y */

	/* absolutex */
	case 0x1d: /* ora $%02x%02x,x */
	case 0x1e: /* asl $%02x%02x,x */
	case 0x3d: /* and $%02x%02x,x */
	case 0x3e: /* rol $%02x%02x,x */
	case 0x5d: /* eor $%02x%02x,x */
	case 0x5e: /* lsr $%02x%02x,x */
	case 0x7d: /* adc $%02x%02x,x */
	case 0x7e: /* ror $%02x%02x,x */
	case 0x9d: /* sta $%02x%02x,x */
	case 0xbc: /* ldy $%02x%02x,x */
	case 0xbd: /* lda $%02x%02x,x */
	case 0xdd: /* cmp $%02x%02x,x */
	case 0xde: /* dec $%02x%02x,x */
	case 0xfd: /* sbc $%02x%02x,x */
	case 0xfe: /* inc $%02x%02x,x */

	/* indirect */
	case 0x6c: /* jmp ($%02x%02x) */
		entry->num_bytes = 3;
		if (pc + 3 > last_pc) goto truncated;
		op1 = *src++;
		entry->instruction[1] = op1;
		op2 = *src;
		entry->instruction[2] = op2;
		addr = (256 * op2) + op1;
		jmp_targets->discovered[addr] = DISASM_6502;
		entry->target_addr = addr;
		entry->flag = FLAG_TARGET_ADDR;
		entry->disassembler_type = DISASM_6502;
		break;


	/* relative */
	case 0x10: /* bpl $%04x */
	case 0x30: /* bmi $%04x */
	case 0x50: /* bvc $%04x */
	case 0x70: /* bvs $%04x */
	case 0x90: /* bcc $%04x */
	case 0xb0: /* bcs $%04x */
	case 0xd0: /* bne $%04x */
	case 0xf0: /* beq $%04x */
		entry->num_bytes = 2;
		if (pc + 2 > last_pc) goto truncated;
		op1 = *src;
		entry->instruction[1] = op1;
		if (op1 > 127) dist = op1 - 256; else dist = op1;
		rel = (pc + 2 + dist) & 0xffff;
		jmp_targets->discovered[rel] = DISASM_6502;
		entry->target_addr = rel;
		entry->flag = FLAG_BRANCH_TAKEN;
		entry->disassembler_type = DISASM_6502;
		break;



	default:
		goto truncated;
	}
	return entry->num_bytes;
truncated:
	entry->num_bytes = 1;
truncated2:
	entry->flag = 0;
	entry->disassembler_type = DISASM_DATA;
	return entry->num_bytes;
}

int parse_entry_65816(history_entry_t *entry, unsigned char *src, unsigned int pc, unsigned int last_pc, jmp_targets_t *jmp_targets) {
	int dist;
	unsigned int rel;
	unsigned short addr;
	unsigned char opcode, op1, op2, op3;
	
	opcode = *src++;
	entry->instruction[0] = opcode;
	entry->pc = (unsigned short)pc;
	entry->target_addr = 0;
	switch(opcode) {
	/* implicit */
	case 0x0: /* brk  */
	case 0x8: /* php  */
	case 0xb: /* phd  */
	case 0x18: /* clc  */
	case 0x1b: /* tcs  */
	case 0x28: /* plp  */
	case 0x2b: /* pld  */
	case 0x38: /* sec  */
	case 0x3b: /* tsc  */
	case 0x40: /* rti  */
	case 0x48: /* pha  */
	case 0x4b: /* phk  */
	case 0x58: /* cli  */
	case 0x5a: /* phy  */
	case 0x5b: /* tcd  */
	case 0x60: /* rts  */
	case 0x68: /* pla  */
	case 0x6b: /* rtl  */
	case 0x78: /* sei  */
	case 0x7a: /* ply  */
	case 0x7b: /* tdc  */
	case 0x88: /* dey  */
	case 0x8a: /* txa  */
	case 0x8b: /* phb  */
	case 0x98: /* tya  */
	case 0x9a: /* txs  */
	case 0x9b: /* txy  */
	case 0xa8: /* tay  */
	case 0xaa: /* tax  */
	case 0xab: /* plb  */
	case 0xb8: /* clv  */
	case 0xba: /* tsx  */
	case 0xbb: /* tyx  */
	case 0xc8: /* iny  */
	case 0xca: /* dex  */
	case 0xcb: /* wai  */
	case 0xd8: /* cld  */
	case 0xda: /* phx  */
	case 0xdb: /* stp  */
	case 0xe8: /* inx  */
	case 0xea: /* nop  */
	case 0xeb: /* xba  */
	case 0xf8: /* sed  */
	case 0xfa: /* plx  */
	case 0xfb: /* xce  */

	/* accumulator */
	case 0xa: /* asl a */
	case 0x1a: /* inc a */
	case 0x2a: /* rol a */
	case 0x3a: /* dec a */
	case 0x4a: /* lsr a */
	case 0x6a: /* ror a */
		entry->num_bytes = 1;
		entry->disassembler_type = DISASM_65816;
		break;


	/* indirectx */
	case 0x1: /* ora ($%02x,x) */
	case 0x21: /* and ($%02x,x) */
	case 0x41: /* eor ($%02x,x) */
	case 0x61: /* adc ($%02x,x) */
	case 0x81: /* sta ($%02x,x) */
	case 0xa1: /* lda ($%02x,x) */
	case 0xc1: /* cmp ($%02x,x) */
	case 0xe1: /* sbc ($%02x,x) */

	/* zeropage */
	case 0x2: /* cop $%02x */
	case 0x4: /* tsb $%02x */
	case 0x5: /* ora $%02x */
	case 0x6: /* asl $%02x */
	case 0x14: /* trb $%02x */
	case 0x24: /* bit $%02x */
	case 0x25: /* and $%02x */
	case 0x26: /* rol $%02x */
	case 0x42: /* wdm $%02x */
	case 0x45: /* eor $%02x */
	case 0x46: /* lsr $%02x */
	case 0x64: /* stz $%02x */
	case 0x65: /* adc $%02x */
	case 0x66: /* ror $%02x */
	case 0x84: /* sty $%02x */
	case 0x85: /* sta $%02x */
	case 0x86: /* stx $%02x */
	case 0xa4: /* ldy $%02x */
	case 0xa5: /* lda $%02x */
	case 0xa6: /* ldx $%02x */
	case 0xc4: /* cpy $%02x */
	case 0xc5: /* cmp $%02x */
	case 0xc6: /* dec $%02x */
	case 0xe4: /* cpx $%02x */
	case 0xe5: /* sbc $%02x */
	case 0xe6: /* inc $%02x */

	/* directpageindirectlong */
	case 0x7: /* ora [$%02x] */
	case 0x27: /* and [$%02x] */
	case 0x47: /* eor [$%02x] */
	case 0x67: /* adc [$%02x] */
	case 0x87: /* sta [$%02x] */
	case 0xa7: /* lda [$%02x] */
	case 0xc7: /* cmp [$%02x] */
	case 0xe7: /* sbc [$%02x] */

	/* indirecty */
	case 0x11: /* ora ($%02x),y */
	case 0x31: /* and ($%02x),y */
	case 0x51: /* eor ($%02x),y */
	case 0x71: /* adc ($%02x),y */
	case 0x91: /* sta ($%02x),y */
	case 0xb1: /* lda ($%02x),y */
	case 0xd1: /* cmp ($%02x),y */
	case 0xf1: /* sbc ($%02x),y */

	/* indirectzeropage */
	case 0x12: /* ora ($%02x) */
	case 0x32: /* and ($%02x) */
	case 0x52: /* eor ($%02x) */
	case 0x72: /* adc ($%02x) */
	case 0x92: /* sta ($%02x) */
	case 0xb2: /* lda ($%02x) */
	case 0xd2: /* cmp ($%02x) */
	case 0xf2: /* sbc ($%02x) */

	/* zeropagex */
	case 0x15: /* ora $%02x,x */
	case 0x16: /* asl $%02x,x */
	case 0x34: /* bit $%02x,x */
	case 0x35: /* and $%02x,x */
	case 0x36: /* rol $%02x,x */
	case 0x55: /* eor $%02x,x */
	case 0x56: /* lsr $%02x,x */
	case 0x74: /* stz $%02x,x */
	case 0x75: /* adc $%02x,x */
	case 0x76: /* ror $%02x,x */
	case 0x94: /* sty $%02x,x */
	case 0x95: /* sta $%02x,x */
	case 0xb4: /* ldy $%02x,x */
	case 0xb5: /* lda $%02x,x */
	case 0xd5: /* cmp $%02x,x */
	case 0xd6: /* dec $%02x,x */
	case 0xf5: /* sbc $%02x,x */
	case 0xf6: /* inc $%02x,x */

	/* directpageindirectlongy */
	case 0x17: /* ora [$%02x],y */
	case 0x37: /* and [$%02x],y */
	case 0x57: /* eor [$%02x],y */
	case 0x77: /* adc [$%02x],y */
	case 0x97: /* sta [$%02x],y */
	case 0xb7: /* lda [$%02x],y */
	case 0xd7: /* cmp [$%02x],y */
	case 0xf7: /* sbc [$%02x],y */

	/* zeropagey */
	case 0x96: /* stx $%02x,y */
	case 0xb6: /* ldx $%02x,y */

	/* directpageindirect */
	case 0xd4: /* pei ($%02x) */
		entry->num_bytes = 2;
		if (pc + 2 > last_pc) goto truncated;
		op1 = *src;
		entry->instruction[1] = op1;
		jmp_targets->discovered[op1] = DISASM_65816;
		entry->target_addr = op1;
		entry->flag = FLAG_TARGET_ADDR;
		entry->disassembler_type = DISASM_65816;
		break;


	/* stackrelative */
	case 0x3: /* ora $%02x,s */
	case 0x23: /* and $%02x,s */
	case 0x43: /* eor $%02x,s */
	case 0x63: /* adc $%02x,s */
	case 0x83: /* sta $%02x,s */
	case 0xa3: /* lda $%02x,s */
	case 0xc3: /* cmp $%02x,s */
	case 0xe3: /* sbc $%02x,s */

	/* immediate */
	case 0x9: /* ora #$%02x */
	case 0x29: /* and #$%02x */
	case 0x49: /* eor #$%02x */
	case 0x69: /* adc #$%02x */
	case 0x89: /* bit #$%02x */
	case 0xa0: /* ldy #$%02x */
	case 0xa2: /* ldx #$%02x */
	case 0xa9: /* lda #$%02x */
	case 0xc0: /* cpy #$%02x */
	case 0xc2: /* rep #$%02x */
	case 0xc9: /* cmp #$%02x */
	case 0xe0: /* cpx #$%02x */
	case 0xe2: /* sep #$%02x */
	case 0xe9: /* sbc #$%02x */

	/* stackrelativeindirecty */
	case 0x13: /* ora ($%02x,s),y */
	case 0x33: /* and ($%02x,s),y */
	case 0x53: /* eor ($%02x,s),y */
	case 0x73: /* adc ($%02x,s),y */
	case 0x93: /* sta ($%02x,s),y */
	case 0xb3: /* lda ($%02x,s),y */
	case 0xd3: /* cmp ($%02x,s),y */
	case 0xf3: /* sbc ($%02x,s),y */
		entry->num_bytes = 2;
		if (pc + 2 > last_pc) goto truncated;
		entry->instruction[1] = *src;
		entry->disassembler_type = DISASM_65816;
		break;


	/* absolute */
	case 0xc: /* tsb $%02x%02x */
	case 0xd: /* ora $%02x%02x */
	case 0xe: /* asl $%02x%02x */
	case 0x1c: /* trb $%02x%02x */
	case 0x20: /* jsr $%02x%02x */
	case 0x2c: /* bit $%02x%02x */
	case 0x2d: /* and $%02x%02x */
	case 0x2e: /* rol $%02x%02x */
	case 0x4c: /* jmp $%02x%02x */
	case 0x4d: /* eor $%02x%02x */
	case 0x4e: /* lsr $%02x%02x */
	case 0x62: /* per $%02x%02x */
	case 0x6d: /* adc $%02x%02x */
	case 0x6e: /* ror $%02x%02x */
	case 0x8c: /* sty $%02x%02x */
	case 0x8d: /* sta $%02x%02x */
	case 0x8e: /* stx $%02x%02x */
	case 0x9c: /* stz $%02x%02x */
	case 0xac: /* ldy $%02x%02x */
	case 0xad: /* lda $%02x%02x */
	case 0xae: /* ldx $%02x%02x */
	case 0xcc: /* cpy $%02x%02x */
	case 0xcd: /* cmp $%02x%02x */
	case 0xce: /* dec $%02x%02x */
	case 0xec: /* cpx $%02x%02x */
	case 0xed: /* sbc $%02x%02x */
	case 0xee: /* inc $%02x%02x */
	case 0xf4: /* pea $%02x%02x */

	/* absolutey */
	case 0x19: /* ora $%02x%02x,y */
	case 0x39: /* and $%02x%02x,y */
	case 0x59: /* eor $%02x%02x,y */
	case 0x79: /* adc $%02x%02x,y */
	case 0x99: /* sta $%02x%02x,y */
	case 0xb9: /* lda $%02x%02x,y */
	case 0xbe: /* ldx $%02x%02x,y */
	case 0xd9: /* cmp $%02x%02x,y */
	case 0xf9: /* sbc $%02x%02x,y */

	/* absolutex */
	case 0x1d: /* ora $%02x%02x,x */
	case 0x1e: /* asl $%02x%02x,x */
	case 0x3c: /* bit $%02x%02x,x */
	case 0x3d: /* and $%02x%02x,x */
	case 0x3e: /* rol $%02x%02x,x */
	case 0x5d: /* eor $%02x%02x,x */
	case 0x5e: /* lsr $%02x%02x,x */
	case 0x7d: /* adc $%02x%02x,x */
	case 0x7e: /* ror $%02x%02x,x */
	case 0x9d: /* sta $%02x%02x,x */
	case 0x9e: /* stz $%02x%02x,x */
	case 0xbc: /* ldy $%02x%02x,x */
	case 0xbd: /* lda $%02x%02x,x */
	case 0xdd: /* cmp $%02x%02x,x */
	case 0xde: /* dec $%02x%02x,x */
	case 0xfd: /* sbc $%02x%02x,x */
	case 0xfe: /* inc $%02x%02x,x */

	/* indirect */
	case 0x6c: /* jmp ($%02x%02x) */

	/* absoluteindexedindirect */
	case 0x7c: /* jmp ($%02x%02x,x) */

	/* absoluteindirectlong */
	case 0xdc: /* jmp [$%02x%02x] */
		entry->num_bytes = 3;
		if (pc + 3 > last_pc) goto truncated;
		op1 = *src++;
		entry->instruction[1] = op1;
		op2 = *src;
		entry->instruction[2] = op2;
		addr = (256 * op2) + op1;
		jmp_targets->discovered[addr] = DISASM_65816;
		entry->target_addr = addr;
		entry->flag = FLAG_TARGET_ADDR;
		entry->disassembler_type = DISASM_65816;
		break;


	/* absolutelong */
	case 0xf: /* ora $%02x%02x%02x */
	case 0x22: /* jsr $%02x%02x%02x */
	case 0x2f: /* and $%02x%02x%02x */
	case 0x4f: /* eor $%02x%02x%02x */
	case 0x5c: /* jmp $%02x%02x%02x */
	case 0x6f: /* adc $%02x%02x%02x */
	case 0x8f: /* sta $%02x%02x%02x */
	case 0xaf: /* lda $%02x%02x%02x */
	case 0xcf: /* cmp $%02x%02x%02x */
	case 0xef: /* sbc $%02x%02x%02x */

	/* absolutelongx */
	case 0x1f: /* ora $%02x%02x%02x,x */
	case 0x3f: /* and $%02x%02x%02x,x */
	case 0x5f: /* eor $%02x%02x%02x,x */
	case 0x7f: /* adc $%02x%02x%02x,x */
	case 0x9f: /* sta $%02x%02x%02x,x */
	case 0xbf: /* lda $%02x%02x%02x,x */
	case 0xdf: /* cmp $%02x%02x%02x,x */
	case 0xff: /* sbc $%02x%02x%02x,x */
		entry->num_bytes = 4;
		if (pc + 4 > last_pc) goto truncated;
		op1 = *src++;
		entry->instruction[1] = op1;
		op2 = *src++;
		entry->instruction[2] = op2;
		op3 = *src;
		entry->instruction[3] = op3;
		addr = (256 * op3) + op2;
		jmp_targets->discovered[addr] = DISASM_65816;
		entry->target_addr = addr;
		entry->flag = FLAG_TARGET_ADDR;
		entry->disassembler_type = DISASM_65816;
		break;


	/* relative */
	case 0x10: /* bpl $%04x */
	case 0x30: /* bmi $%04x */
	case 0x50: /* bvc $%04x */
	case 0x70: /* bvs $%04x */
	case 0x80: /* bra $%04x */
	case 0x90: /* bcc $%04x */
	case 0xb0: /* bcs $%04x */
	case 0xd0: /* bne $%04x */
	case 0xf0: /* beq $%04x */
		entry->num_bytes = 2;
		if (pc + 2 > last_pc) goto truncated;
		op1 = *src;
		entry->instruction[1] = op1;
		if (op1 > 127) dist = op1 - 256; else dist = op1;
		rel = (pc + 2 + dist) & 0xffff;
		jmp_targets->discovered[rel] = DISASM_65816;
		entry->target_addr = rel;
		entry->flag = FLAG_BRANCH_TAKEN;
		entry->disassembler_type = DISASM_65816;
		break;


	/* blockmove */
	case 0x44: /* mvp $%02x,$%02x */
	case 0x54: /* mvn $%02x,$%02x */
		entry->num_bytes = 3;
		if (pc + 3 > last_pc) goto truncated;
		op1 = *src++;
		entry->instruction[1] = op1;
		op2 = *src;
		entry->instruction[2] = op2;
		addr = (256 * op1) + op2;
		jmp_targets->discovered[addr] = DISASM_65816;
		entry->target_addr = addr;
		entry->flag = FLAG_TARGET_ADDR;
		entry->disassembler_type = DISASM_65816;
		break;


	/* relativelong */
	case 0x82: /* brl $%04x */
		entry->num_bytes = 3;
		if (pc + 3 > last_pc) goto truncated;
		op1 = *src++;
		entry->instruction[1] = op1;
		op2 = *src;
		entry->instruction[2] = op2;
		entry->flag = FLAG_BRANCH_TAKEN;
		entry->disassembler_type = DISASM_65816;
		break;



	default:
		goto truncated;
	}
	return entry->num_bytes;
truncated:
	entry->num_bytes = 1;
truncated2:
	entry->flag = 0;
	entry->disassembler_type = DISASM_DATA;
	return entry->num_bytes;
}

int parse_entry_65c02(history_entry_t *entry, unsigned char *src, unsigned int pc, unsigned int last_pc, jmp_targets_t *jmp_targets) {
	int dist;
	unsigned int rel;
	unsigned short addr;
	unsigned char opcode, op1, op2, op3;
	
	opcode = *src++;
	entry->instruction[0] = opcode;
	entry->pc = (unsigned short)pc;
	entry->target_addr = 0;
	switch(opcode) {
	/* implicit */
	case 0x0: /* brk  */
	case 0x8: /* php  */
	case 0x18: /* clc  */
	case 0x28: /* plp  */
	case 0x38: /* sec  */
	case 0x40: /* rti  */
	case 0x48: /* pha  */
	case 0x58: /* cli  */
	case 0x5a: /* phy  */
	case 0x60: /* rts  */
	case 0x68: /* pla  */
	case 0x78: /* sei  */
	case 0x7a: /* ply  */
	case 0x88: /* dey  */
	case 0x8a: /* txa  */
	case 0x98: /* tya  */
	case 0x9a: /* txs  */
	case 0xa8: /* tay  */
	case 0xaa: /* tax  */
	case 0xb8: /* clv  */
	case 0xba: /* tsx  */
	case 0xc8: /* iny  */
	case 0xca: /* dex  */
	case 0xcb: /* wai  */
	case 0xd8: /* cld  */
	case 0xda: /* phx  */
	case 0xdb: /* stp  */
	case 0xe8: /* inx  */
	case 0xea: /* nop  */
	case 0xf8: /* sed  */
	case 0xfa: /* plx  */

	/* accumulator */
	case 0xa: /* asl a */
	case 0x1a: /* inc a */
	case 0x2a: /* rol a */
	case 0x3a: /* dec a */
	case 0x4a: /* lsr a */
	case 0x6a: /* ror a */
		entry->num_bytes = 1;
		entry->disassembler_type = DISASM_65C02;
		break;


	/* indirectx */
	case 0x1: /* ora ($%02x,x) */
	case 0x21: /* and ($%02x,x) */
	case 0x41: /* eor ($%02x,x) */
	case 0x61: /* adc ($%02x,x) */
	case 0x81: /* sta ($%02x,x) */
	case 0xa1: /* lda ($%02x,x) */
	case 0xc1: /* cmp ($%02x,x) */
	case 0xe1: /* sbc ($%02x,x) */

	/* zeropage */
	case 0x4: /* tsb $%02x */
	case 0x5: /* ora $%02x */
	case 0x6: /* asl $%02x */
	case 0x7: /* rmb0 $%02x */
	case 0x14: /* trb $%02x */
	case 0x17: /* rmb1 $%02x */
	case 0x24: /* bit $%02x */
	case 0x25: /* and $%02x */
	case 0x26: /* rol $%02x */
	case 0x27: /* rmb2 $%02x */
	case 0x37: /* rmb3 $%02x */
	case 0x45: /* eor $%02x */
	case 0x46: /* lsr $%02x */
	case 0x47: /* rmb4 $%02x */
	case 0x57: /* rmb5 $%02x */
	case 0x64: /* stz $%02x */
	case 0x65: /* adc $%02x */
	case 0x66: /* ror $%02x */
	case 0x67: /* rmb6 $%02x */
	case 0x77: /* rmb7 $%02x */
	case 0x84: /* sty $%02x */
	case 0x85: /* sta $%02x */
	case 0x86: /* stx $%02x */
	case 0x87: /* smb0 $%02x */
	case 0x97: /* smb1 $%02x */
	case 0xa4: /* ldy $%02x */
	case 0xa5: /* lda $%02x */
	case 0xa6: /* ldx $%02x */
	case 0xa7: /* smb2 $%02x */
	case 0xb7: /* smb3 $%02x */
	case 0xc4: /* cpy $%02x */
	case 0xc5: /* cmp $%02x */
	case 0xc6: /* dec $%02x */
	case 0xc7: /* smb4 $%02x */
	case 0xd7: /* smb5 $%02x */
	case 0xe4: /* cpx $%02x */
	case 0xe5: /* sbc $%02x */
	case 0xe6: /* inc $%02x */
	case 0xe7: /* smb6 $%02x */
	case 0xf7: /* smb7 $%02x */

	/* indirecty */
	case 0x11: /* ora ($%02x),y */
	case 0x31: /* and ($%02x),y */
	case 0x51: /* eor ($%02x),y */
	case 0x71: /* adc ($%02x),y */
	case 0x91: /* sta ($%02x),y */
	case 0xb1: /* lda ($%02x),y */
	case 0xd1: /* cmp ($%02x),y */
	case 0xf1: /* sbc ($%02x),y */

	/* zeropagex */
	case 0x15: /* ora $%02x,x */
	case 0x16: /* asl $%02x,x */
	case 0x34: /* bit $%02x,x */
	case 0x35: /* and $%02x,x */
	case 0x36: /* rol $%02x,x */
	case 0x55: /* eor $%02x,x */
	case 0x56: /* lsr $%02x,x */
	case 0x74: /* stz $%02x,x */
	case 0x75: /* adc $%02x,x */
	case 0x76: /* ror $%02x,x */
	case 0x94: /* sty $%02x,x */
	case 0x95: /* sta $%02x,x */
	case 0xb4: /* ldy $%02x,x */
	case 0xb5: /* lda $%02x,x */
	case 0xd5: /* cmp $%02x,x */
	case 0xd6: /* dec $%02x,x */
	case 0xf5: /* sbc $%02x,x */
	case 0xf6: /* inc $%02x,x */

	/* zeropagey */
	case 0x96: /* stx $%02x,y */
	case 0xb6: /* ldx $%02x,y */
		entry->num_bytes = 2;
		if (pc + 2 > last_pc) goto truncated;
		op1 = *src;
		entry->instruction[1] = op1;
		jmp_targets->discovered[op1] = DISASM_65C02;
		entry->target_addr = op1;
		entry->flag = FLAG_TARGET_ADDR;
		entry->disassembler_type = DISASM_65C02;
		break;


	/* immediate */
	case 0x9: /* ora #$%02x */
	case 0x29: /* and #$%02x */
	case 0x49: /* eor #$%02x */
	case 0x69: /* adc #$%02x */
	case 0x89: /* bit #$%02x */
	case 0xa0: /* ldy #$%02x */
	case 0xa2: /* ldx #$%02x */
	case 0xa9: /* lda #$%02x */
	case 0xc0: /* cpy #$%02x */
	case 0xc9: /* cmp #$%02x */
	case 0xe0: /* cpx #$%02x */
	case 0xe9: /* sbc #$%02x */

	/* indirectzeropage */
	case 0x12: /* ora ($%02x) */
	case 0x32: /* and ($%02x) */
	case 0x52: /* eor ($%02x) */
	case 0x72: /* adc ($%02x) */
	case 0x92: /* sta ($%02x) */
	case 0xb2: /* lda ($%02x) */
	case 0xd2: /* cmp ($%02x) */
	case 0xf2: /* sbc ($%02x) */
		entry->num_bytes = 2;
		if (pc + 2 > last_pc) goto truncated;
		entry->instruction[1] = *src;
		entry->disassembler_type = DISASM_65C02;
		break;


	/* absolute */
	case 0xc: /* tsb $%02x%02x */
	case 0xd: /* ora $%02x%02x */
	case 0xe: /* asl $%02x%02x */
	case 0x1c: /* trb $%02x%02x */
	case 0x20: /* jsr $%02x%02x */
	case 0x2c: /* bit $%02x%02x */
	case 0x2d: /* and $%02x%02x */
	case 0x2e: /* rol $%02x%02x */
	case 0x4c: /* jmp $%02x%02x */
	case 0x4d: /* eor $%02x%02x */
	case 0x4e: /* lsr $%02x%02x */
	case 0x6d: /* adc $%02x%02x */
	case 0x6e: /* ror $%02x%02x */
	case 0x8c: /* sty $%02x%02x */
	case 0x8d: /* sta $%02x%02x */
	case 0x8e: /* stx $%02x%02x */
	case 0x9c: /* stz $%02x%02x */
	case 0xac: /* ldy $%02x%02x */
	case 0xad: /* lda $%02x%02x */
	case 0xae: /* ldx $%02x%02x */
	case 0xcc: /* cpy $%02x%02x */
	case 0xcd: /* cmp $%02x%02x */
	case 0xce: /* dec $%02x%02x */
	case 0xec: /* cpx $%02x%02x */
	case 0xed: /* sbc $%02x%02x */
	case 0xee: /* inc $%02x%02x */

	/* absolutey */
	case 0x19: /* ora $%02x%02x,y */
	case 0x39: /* and $%02x%02x,y */
	case 0x59: /* eor $%02x%02x,y */
	case 0x79: /* adc $%02x%02x,y */
	case 0x99: /* sta $%02x%02x,y */
	case 0xb9: /* lda $%02x%02x,y */
	case 0xbe: /* ldx $%02x%02x,y */
	case 0xd9: /* cmp $%02x%02x,y */
	case 0xf9: /* sbc $%02x%02x,y */

	/* absolutex */
	case 0x1d: /* ora $%02x%02x,x */
	case 0x1e: /* asl $%02x%02x,x */
	case 0x3c: /* bit $%02x%02x,x */
	case 0x3d: /* and $%02x%02x,x */
	case 0x3e: /* rol $%02x%02x,x */
	case 0x5d: /* eor $%02x%02x,x */
	case 0x5e: /* lsr $%02x%02x,x */
	case 0x7d: /* adc $%02x%02x,x */
	case 0x7e: /* ror $%02x%02x,x */
	case 0x9d: /* sta $%02x%02x,x */
	case 0x9e: /* stz $%02x%02x,x */
	case 0xbc: /* ldy $%02x%02x,x */
	case 0xbd: /* lda $%02x%02x,x */
	case 0xdd: /* cmp $%02x%02x,x */
	case 0xde: /* dec $%02x%02x,x */
	case 0xfd: /* sbc $%02x%02x,x */
	case 0xfe: /* inc $%02x%02x,x */

	/* indirect */
	case 0x6c: /* jmp ($%02x%02x) */

	/* absoluteindexedindirect */
	case 0x7c: /* jmp ($%02x%02x,x) */
		entry->num_bytes = 3;
		if (pc + 3 > last_pc) goto truncated;
		op1 = *src++;
		entry->instruction[1] = op1;
		op2 = *src;
		entry->instruction[2] = op2;
		addr = (256 * op2) + op1;
		jmp_targets->discovered[addr] = DISASM_65C02;
		entry->target_addr = addr;
		entry->flag = FLAG_TARGET_ADDR;
		entry->disassembler_type = DISASM_65C02;
		break;


	/* zeropagerelative */
	case 0xf: /* bbr0 $%02x,${1:04x} */
	case 0x1f: /* bbr1 $%02x,${1:04x} */
	case 0x2f: /* bbr2 $%02x,${1:04x} */
	case 0x3f: /* bbr3 $%02x,${1:04x} */
	case 0x4f: /* bbr4 $%02x,${1:04x} */
	case 0x5f: /* bbr5 $%02x,${1:04x} */
	case 0x6f: /* bbr6 $%02x,${1:04x} */
	case 0x7f: /* bbr7 $%02x,${1:04x} */
	case 0x8f: /* bbs0 $%02x,${1:04x} */
	case 0x9f: /* bbs1 $%02x,${1:04x} */
	case 0xaf: /* bbs2 $%02x,${1:04x} */
	case 0xbf: /* bbs3 $%02x,${1:04x} */
	case 0xcf: /* bbs4 $%02x,${1:04x} */
	case 0xdf: /* bbs5 $%02x,${1:04x} */
	case 0xef: /* bbs6 $%02x,${1:04x} */
	case 0xff: /* bbs7 $%02x,${1:04x} */
		entry->num_bytes = 3;
		if (pc + 3 > last_pc) goto truncated;
		op1 = *src++;
		entry->instruction[1] = op1;
		op2 = *src;
		entry->instruction[2] = op2;
		entry->flag = FLAG_BRANCH_TAKEN;
		entry->disassembler_type = DISASM_65C02;
		break;


	/* relative */
	case 0x10: /* bpl $%04x */
	case 0x30: /* bmi $%04x */
	case 0x50: /* bvc $%04x */
	case 0x70: /* bvs $%04x */
	case 0x80: /* bra $%04x */
	case 0x90: /* bcc $%04x */
	case 0xb0: /* bcs $%04x */
	case 0xd0: /* bne $%04x */
	case 0xf0: /* beq $%04x */
		entry->num_bytes = 2;
		if (pc + 2 > last_pc) goto truncated;
		op1 = *src;
		entry->instruction[1] = op1;
		if (op1 > 127) dist = op1 - 256; else dist = op1;
		rel = (pc + 2 + dist) & 0xffff;
		jmp_targets->discovered[rel] = DISASM_65C02;
		entry->target_addr = rel;
		entry->flag = FLAG_BRANCH_TAKEN;
		entry->disassembler_type = DISASM_65C02;
		break;



	default:
		goto truncated;
	}
	return entry->num_bytes;
truncated:
	entry->num_bytes = 1;
truncated2:
	entry->flag = 0;
	entry->disassembler_type = DISASM_DATA;
	return entry->num_bytes;
}

int parse_entry_6800(history_entry_t *entry, unsigned char *src, unsigned int pc, unsigned int last_pc, jmp_targets_t *jmp_targets) {
	int dist;
	unsigned int rel;
	unsigned short addr;
	unsigned char opcode, op1, op2, op3;
	
	opcode = *src++;
	entry->instruction[0] = opcode;
	entry->pc = (unsigned short)pc;
	entry->target_addr = 0;
	switch(opcode) {
	/* implied */
	case 0x1: /* nop  */
	case 0x6: /* tap  */
	case 0x7: /* tpa  */
	case 0x8: /* inx  */
	case 0x9: /* dex  */
	case 0xa: /* clv  */
	case 0xb: /* sev  */
	case 0xc: /* clc  */
	case 0xd: /* sec  */
	case 0xe: /* cli  */
	case 0xf: /* sei  */
	case 0x10: /* sba  */
	case 0x11: /* cba  */
	case 0x16: /* tab  */
	case 0x17: /* tba  */
	case 0x19: /* daa  */
	case 0x1b: /* aba  */
	case 0x30: /* tsx  */
	case 0x31: /* ins  */
	case 0x32: /* pula  */
	case 0x33: /* pulb  */
	case 0x34: /* des  */
	case 0x35: /* txs  */
	case 0x36: /* psha  */
	case 0x37: /* pshb  */
	case 0x39: /* rts  */
	case 0x3b: /* rti  */
	case 0x3e: /* wai  */
	case 0x3f: /* swi  */
	case 0x40: /* nega  */
	case 0x43: /* coma  */
	case 0x44: /* lsra  */
	case 0x46: /* rora  */
	case 0x47: /* asra  */
	case 0x48: /* asla  */
	case 0x49: /* rola  */
	case 0x4a: /* deca  */
	case 0x4c: /* inca  */
	case 0x4d: /* tsta  */
	case 0x4f: /* clra  */
	case 0x50: /* negb  */
	case 0x53: /* comb  */
	case 0x54: /* lsrb  */
	case 0x56: /* rorb  */
	case 0x57: /* asrb  */
	case 0x58: /* aslb  */
	case 0x59: /* rolb  */
	case 0x5a: /* decb  */
	case 0x5c: /* incb  */
	case 0x5d: /* tstb  */
	case 0x5f: /* clrb  */
		entry->num_bytes = 1;
		entry->disassembler_type = DISASM_6800;
		break;


	/* relative */
	case 0x20: /* bra $%04x */
	case 0x22: /* bhi $%04x */
	case 0x23: /* bls $%04x */
	case 0x24: /* bcc $%04x */
	case 0x25: /* bcs $%04x */
	case 0x26: /* bne $%04x */
	case 0x27: /* beq $%04x */
	case 0x28: /* bvc $%04x */
	case 0x29: /* bvs $%04x */
	case 0x2a: /* bpl $%04x */
	case 0x2b: /* bmi $%04x */
	case 0x2c: /* bge $%04x */
	case 0x2d: /* blt $%04x */
	case 0x2e: /* bgt $%04x */
	case 0x2f: /* ble $%04x */
	case 0x8d: /* bsr $%04x */
		entry->num_bytes = 2;
		if (pc + 2 > last_pc) goto truncated;
		op1 = *src;
		entry->instruction[1] = op1;
		if (op1 > 127) dist = op1 - 256; else dist = op1;
		rel = (pc + 2 + dist) & 0xffff;
		jmp_targets->discovered[rel] = DISASM_6800;
		entry->target_addr = rel;
		entry->flag = FLAG_BRANCH_TAKEN;
		entry->disassembler_type = DISASM_6800;
		break;


	/* indexed */
	case 0x60: /* neg $%02x,x */
	case 0x63: /* com $%02x,x */
	case 0x64: /* lsr $%02x,x */
	case 0x66: /* ror $%02x,x */
	case 0x67: /* asr $%02x,x */
	case 0x68: /* asl $%02x,x */
	case 0x69: /* rol $%02x,x */
	case 0x6a: /* dec $%02x,x */
	case 0x6c: /* inc $%02x,x */
	case 0x6d: /* tst $%02x,x */
	case 0x6e: /* jmp $%02x,x */
	case 0x6f: /* clr $%02x,x */
	case 0xa0: /* suba $%02x,x */
	case 0xa1: /* cmpa $%02x,x */
	case 0xa2: /* sbca $%02x,x */
	case 0xa4: /* anda $%02x,x */
	case 0xa5: /* bita $%02x,x */
	case 0xa6: /* ldaa $%02x,x */
	case 0xa7: /* staa $%02x,x */
	case 0xa8: /* eora $%02x,x */
	case 0xa9: /* adca $%02x,x */
	case 0xaa: /* oraa $%02x,x */
	case 0xab: /* adda $%02x,x */
	case 0xac: /* cpx $%02x,x */
	case 0xad: /* jsr $%02x,x */
	case 0xae: /* lds $%02x,x */
	case 0xaf: /* sts $%02x,x */
	case 0xe0: /* subb $%02x,x */
	case 0xe1: /* cmpb $%02x,x */
	case 0xe2: /* sbcb $%02x,x */
	case 0xe4: /* andb $%02x,x */
	case 0xe5: /* bitb $%02x,x */
	case 0xe6: /* ldab $%02x,x */
	case 0xe7: /* stab $%02x,x */
	case 0xe8: /* eorb $%02x,x */
	case 0xe9: /* adcb $%02x,x */
	case 0xea: /* orab $%02x,x */
	case 0xeb: /* addb $%02x,x */
	case 0xee: /* ldx $%02x,x */
	case 0xef: /* stx $%02x,x */

	/* direct */
	case 0x90: /* suba $%02x */
	case 0x91: /* cmpa $%02x */
	case 0x92: /* sbca $%02x */
	case 0x94: /* anda $%02x */
	case 0x95: /* bita $%02x */
	case 0x96: /* ldaa $%02x */
	case 0x97: /* staa $%02x */
	case 0x98: /* eora $%02x */
	case 0x99: /* adca $%02x */
	case 0x9a: /* oraa $%02x */
	case 0x9b: /* adda $%02x */
	case 0x9c: /* cpx $%02x */
	case 0x9e: /* lds $%02x */
	case 0x9f: /* sts $%02x */
	case 0xd0: /* subb $%02x */
	case 0xd1: /* cmpb $%02x */
	case 0xd2: /* sbcb $%02x */
	case 0xd4: /* andb $%02x */
	case 0xd5: /* bitb $%02x */
	case 0xd6: /* ldab $%02x */
	case 0xd7: /* stab $%02x */
	case 0xd8: /* eorb $%02x */
	case 0xd9: /* adcb $%02x */
	case 0xda: /* orab $%02x */
	case 0xdb: /* addb $%02x */
	case 0xde: /* ldx $%02x */
	case 0xdf: /* stx $%02x */
		entry->num_bytes = 2;
		if (pc + 2 > last_pc) goto truncated;
		op1 = *src;
		entry->instruction[1] = op1;
		jmp_targets->discovered[op1] = DISASM_6800;
		entry->target_addr = op1;
		entry->flag = FLAG_TARGET_ADDR;
		entry->disassembler_type = DISASM_6800;
		break;


	/* extended */
	case 0x70: /* neg $%02x%02x */
	case 0x73: /* com $%02x%02x */
	case 0x74: /* lsr $%02x%02x */
	case 0x76: /* ror $%02x%02x */
	case 0x77: /* asr $%02x%02x */
	case 0x78: /* asl $%02x%02x */
	case 0x79: /* rol $%02x%02x */
	case 0x7a: /* dec $%02x%02x */
	case 0x7c: /* inc $%02x%02x */
	case 0x7d: /* tst $%02x%02x */
	case 0x7e: /* jmp $%02x%02x */
	case 0x7f: /* clr $%02x%02x */
	case 0xb0: /* suba $%02x%02x */
	case 0xb1: /* cmpa $%02x%02x */
	case 0xb2: /* sbca $%02x%02x */
	case 0xb4: /* anda $%02x%02x */
	case 0xb5: /* bita $%02x%02x */
	case 0xb6: /* ldaa $%02x%02x */
	case 0xb7: /* staa $%02x%02x */
	case 0xb8: /* eora $%02x%02x */
	case 0xb9: /* adca $%02x%02x */
	case 0xba: /* oraa $%02x%02x */
	case 0xbb: /* adda $%02x%02x */
	case 0xbc: /* cpx $%02x%02x */
	case 0xbd: /* jsr $%02x%02x */
	case 0xbe: /* lds $%02x%02x */
	case 0xbf: /* sts $%02x%02x */
	case 0xf0: /* subb $%02x%02x */
	case 0xf1: /* cmpb $%02x%02x */
	case 0xf2: /* sbcb $%02x%02x */
	case 0xf4: /* andb $%02x%02x */
	case 0xf5: /* bitb $%02x%02x */
	case 0xf6: /* ldab $%02x%02x */
	case 0xf7: /* stab $%02x%02x */
	case 0xf8: /* eorb $%02x%02x */
	case 0xf9: /* adcb $%02x%02x */
	case 0xfa: /* orab $%02x%02x */
	case 0xfb: /* addb $%02x%02x */
	case 0xfe: /* ldx $%02x%02x */
	case 0xff: /* stx $%02x%02x */
		entry->num_bytes = 3;
		if (pc + 3 > last_pc) goto truncated;
		op1 = *src++;
		entry->instruction[1] = op1;
		op2 = *src;
		entry->instruction[2] = op2;
		addr = (256 * op1) + op2;
		jmp_targets->discovered[addr] = DISASM_6800;
		entry->target_addr = addr;
		entry->flag = FLAG_TARGET_ADDR;
		entry->disassembler_type = DISASM_6800;
		break;


	/* immediate */
	case 0x80: /* suba #$%02x */
	case 0x81: /* cmpa #$%02x */
	case 0x82: /* sbca #$%02x */
	case 0x84: /* anda #$%02x */
	case 0x85: /* bita #$%02x */
	case 0x86: /* ldaa #$%02x */
	case 0x88: /* eora #$%02x */
	case 0x89: /* adca #$%02x */
	case 0x8a: /* oraa #$%02x */
	case 0x8b: /* adda #$%02x */
	case 0xc0: /* subb #$%02x */
	case 0xc1: /* cmpb #$%02x */
	case 0xc2: /* sbcb #$%02x */
	case 0xc4: /* andb #$%02x */
	case 0xc5: /* bitb #$%02x */
	case 0xc6: /* ldab #$%02x */
	case 0xc8: /* eorb #$%02x */
	case 0xc9: /* adcb #$%02x */
	case 0xca: /* orab #$%02x */
	case 0xcb: /* addb #$%02x */
		entry->num_bytes = 2;
		if (pc + 2 > last_pc) goto truncated;
		entry->instruction[1] = *src;
		entry->disassembler_type = DISASM_6800;
		break;


	/* immediatex */
	case 0x8c: /* cpx #$%02x%02x */
	case 0x8e: /* lds #$%02x%02x */
	case 0xce: /* ldx #$%02x%02x */
		entry->num_bytes = 3;
		if (pc + 3 > last_pc) goto truncated;
		op1 = *src++;
		entry->instruction[1] = op1;
		op2 = *src;
		entry->instruction[2] = op2;
		entry->disassembler_type = DISASM_6800;
		break;



	default:
		goto truncated;
	}
	return entry->num_bytes;
truncated:
	entry->num_bytes = 1;
truncated2:
	entry->flag = 0;
	entry->disassembler_type = DISASM_DATA;
	return entry->num_bytes;
}

int parse_entry_6809(history_entry_t *entry, unsigned char *src, unsigned int pc, unsigned int last_pc, jmp_targets_t *jmp_targets) {
	int dist;
	unsigned int rel;
	unsigned short addr;
	unsigned char opcode, op1, op2, op3;
	
	opcode = *src++;
	entry->instruction[0] = opcode;
	entry->pc = (unsigned short)pc;
	entry->target_addr = 0;
	switch(opcode) {
	/* direct */
	case 0x0: /* neg $%02x */
	case 0x3: /* comb $%02x */
	case 0x4: /* lsr $%02x */
	case 0x6: /* ror $%02x */
	case 0x7: /* asr $%02x */
	case 0x8: /* lsl $%02x */
	case 0x9: /* rol $%02x */
	case 0xa: /* dec $%02x */
	case 0xd: /* tst $%02x */
	case 0xf: /* clr $%02x */
	case 0x6c: /* inc $%02x */
	case 0x6e: /* jmp $%02x */
	case 0x90: /* suba $%02x */
	case 0x91: /* cmpa $%02x */
	case 0x92: /* sbca $%02x */
	case 0x93: /* subd $%02x */
	case 0x94: /* anda $%02x */
	case 0x95: /* bita $%02x */
	case 0x96: /* lda $%02x */
	case 0x97: /* sta $%02x */
	case 0x98: /* eora $%02x */
	case 0x99: /* adca $%02x */
	case 0x9a: /* ora $%02x */
	case 0x9b: /* adda $%02x */
	case 0x9c: /* cmpx $%02x */
	case 0x9e: /* ldx $%02x */
	case 0x9f: /* stx $%02x */
	case 0xa8: /* eora $%02x */
	case 0xad: /* jsr $%02x */
	case 0xd0: /* subb $%02x */
	case 0xd1: /* cmpb $%02x */
	case 0xd2: /* sbcb $%02x */
	case 0xd3: /* addd $%02x */
	case 0xd4: /* andb $%02x */
	case 0xd5: /* bitb $%02x */
	case 0xd6: /* ldb $%02x */
	case 0xd7: /* stb $%02x */
	case 0xd8: /* eorb $%02x */
	case 0xd9: /* adcb $%02x */
	case 0xda: /* orb $%02x */
	case 0xdb: /* addb $%02x */
	case 0xdc: /* ldd $%02x */
	case 0xdd: /* std $%02x */
	case 0xde: /* ldu $%02x */
	case 0xdf: /* stu $%02x */
	case 0xe8: /* eorb $%02x */

	/* indexed */
	case 0xc: /* inc $%02x,x */
	case 0xe: /* jmp $%02x,x */
	case 0x30: /* leax $%02x,x */
	case 0x31: /* leay $%02x,x */
	case 0x32: /* leas $%02x,x */
	case 0x33: /* leau $%02x,x */
	case 0x60: /* neg $%02x,x */
	case 0x63: /* comb $%02x,x */
	case 0x64: /* lsr $%02x,x */
	case 0x66: /* ror $%02x,x */
	case 0x67: /* asr $%02x,x */
	case 0x68: /* lsl $%02x,x */
	case 0x69: /* rol $%02x,x */
	case 0x6a: /* dec $%02x,x */
	case 0x6d: /* tst $%02x,x */
	case 0x6f: /* clr $%02x,x */
	case 0x9d: /* jsr $%02x,x */
	case 0xa0: /* suba $%02x,x */
	case 0xa1: /* cmpa $%02x,x */
	case 0xa2: /* sbca $%02x,x */
	case 0xa3: /* subd $%02x,x */
	case 0xa4: /* anda $%02x,x */
	case 0xa5: /* bita $%02x,x */
	case 0xa6: /* lda $%02x,x */
	case 0xa7: /* sta $%02x,x */
	case 0xa9: /* adca $%02x,x */
	case 0xaa: /* ora $%02x,x */
	case 0xab: /* adda $%02x,x */
	case 0xac: /* cmpx $%02x,x */
	case 0xae: /* ldx $%02x,x */
	case 0xaf: /* stx $%02x,x */
	case 0xe0: /* subb $%02x,x */
	case 0xe1: /* cmpb $%02x,x */
	case 0xe2: /* sbcb $%02x,x */
	case 0xe3: /* addd $%02x,x */
	case 0xe4: /* andb $%02x,x */
	case 0xe5: /* bitb $%02x,x */
	case 0xe6: /* ldb $%02x,x */
	case 0xe7: /* stb $%02x,x */
	case 0xe9: /* adcb $%02x,x */
	case 0xea: /* orb $%02x,x */
	case 0xeb: /* addb $%02x,x */
	case 0xec: /* ldd $%02x,x */
	case 0xed: /* std $%02x,x */
	case 0xee: /* ldu $%02x,x */
	case 0xef: /* stu $%02x,x */
		entry->num_bytes = 2;
		if (pc + 2 > last_pc) goto truncated;
		op1 = *src;
		entry->instruction[1] = op1;
		jmp_targets->discovered[op1] = DISASM_6809;
		entry->target_addr = op1;
		entry->flag = FLAG_TARGET_ADDR;
		entry->disassembler_type = DISASM_6809;
		break;


	/* inherent */
	case 0x12: /* nop  */
	case 0x13: /* sync  */
	case 0x19: /* daa  */
	case 0x1d: /* sex  */
	case 0x39: /* rts  */
	case 0x3a: /* abx  */
	case 0x3b: /* rti  */
	case 0x3d: /* mul  */
	case 0x3f: /* swi  */
	case 0x40: /* nega  */
	case 0x43: /* coma  */
	case 0x44: /* lsra  */
	case 0x46: /* rora  */
	case 0x47: /* asra  */
	case 0x48: /* lsla  */
	case 0x49: /* rola  */
	case 0x4a: /* deca  */
	case 0x4c: /* inca  */
	case 0x4d: /* tsta  */
	case 0x4f: /* clra  */
	case 0x50: /* negb  */
	case 0x53: /* comb  */
	case 0x54: /* lsrb  */
	case 0x56: /* rorb  */
	case 0x57: /* asrb  */
	case 0x58: /* lslb  */
	case 0x59: /* rolb  */
	case 0x5a: /* decb  */
	case 0x5c: /* incb  */
	case 0x5d: /* tstb  */
	case 0x5f: /* clrb  */
		entry->num_bytes = 1;
		entry->disassembler_type = DISASM_6809;
		break;


	/* rel16 */
	case 0x16: /* lbra $%04x */
	case 0x17: /* lbsr $%04x */
		entry->num_bytes = 3;
		if (pc + 3 > last_pc) goto truncated;
		op1 = *src++;
		entry->instruction[1] = op1;
		op2 = *src;
		entry->instruction[2] = op2;
		entry->flag = FLAG_BRANCH_TAKEN;
		entry->disassembler_type = DISASM_6809;
		break;


	/* imm8 */
	case 0x1a: /* orcc #$%02x */
	case 0x1c: /* andcc #$%02x */
	case 0x34: /* pshs #$%02x */
	case 0x35: /* puls #$%02x */
	case 0x36: /* pshu #$%02x */
	case 0x37: /* pulu #$%02x */
	case 0x3c: /* cwai #$%02x */
	case 0x80: /* suba #$%02x */
	case 0x81: /* cmpa #$%02x */
	case 0x82: /* sbca #$%02x */
	case 0x84: /* anda #$%02x */
	case 0x85: /* bita #$%02x */
	case 0x86: /* lda #$%02x */
	case 0x88: /* eora #$%02x */
	case 0x89: /* adca #$%02x */
	case 0x8a: /* ora #$%02x */
	case 0x8b: /* adda #$%02x */
	case 0xc0: /* subb #$%02x */
	case 0xc1: /* cmpb #$%02x */
	case 0xc2: /* sbcb #$%02x */
	case 0xc4: /* andb #$%02x */
	case 0xc5: /* bitb #$%02x */
	case 0xc6: /* ldb #$%02x */
	case 0xc8: /* eorb #$%02x */
	case 0xc9: /* adcb #$%02x */
	case 0xca: /* orb #$%02x */
	case 0xcb: /* addb #$%02x */

	/* r1,r2 */
	case 0x1e: /* exg $%02x */
	case 0x1f: /* tfr $%02x */
		entry->num_bytes = 2;
		if (pc + 2 > last_pc) goto truncated;
		entry->instruction[1] = *src;
		entry->disassembler_type = DISASM_6809;
		break;


	/* rel8 */
	case 0x20: /* bra $%04x */
	case 0x21: /* brn $%04x */
	case 0x22: /* bhi $%04x */
	case 0x23: /* bls $%04x */
	case 0x24: /* bhs $%04x */
	case 0x25: /* blo $%04x */
	case 0x26: /* bne $%04x */
	case 0x27: /* beq $%04x */
	case 0x28: /* bvc $%04x */
	case 0x29: /* bvs $%04x */
	case 0x2a: /* bpl $%04x */
	case 0x2b: /* bmi $%04x */
	case 0x2c: /* bge $%04x */
	case 0x2d: /* blt $%04x */
	case 0x2e: /* bgt $%04x */
	case 0x2f: /* ble $%04x */
	case 0x8d: /* bsr $%04x */
		entry->num_bytes = 2;
		if (pc + 2 > last_pc) goto truncated;
		op1 = *src;
		entry->instruction[1] = op1;
		if (op1 > 127) dist = op1 - 256; else dist = op1;
		rel = (pc + 2 + dist) & 0xffff;
		jmp_targets->discovered[rel] = DISASM_6809;
		entry->target_addr = rel;
		entry->flag = FLAG_BRANCH_TAKEN;
		entry->disassembler_type = DISASM_6809;
		break;


	/* extended */
	case 0x70: /* neg $%02x%02x */
	case 0x73: /* comb $%02x%02x */
	case 0x74: /* lsr $%02x%02x */
	case 0x76: /* ror $%02x%02x */
	case 0x77: /* asr $%02x%02x */
	case 0x78: /* lsl $%02x%02x */
	case 0x79: /* rol $%02x%02x */
	case 0x7a: /* dec $%02x%02x */
	case 0x7c: /* inc $%02x%02x */
	case 0x7d: /* tst $%02x%02x */
	case 0x7e: /* jmp $%02x%02x */
	case 0x7f: /* clr $%02x%02x */
	case 0xb0: /* suba $%02x%02x */
	case 0xb1: /* cmpa $%02x%02x */
	case 0xb2: /* sbca $%02x%02x */
	case 0xb3: /* subd $%02x%02x */
	case 0xb4: /* anda $%02x%02x */
	case 0xb5: /* bita $%02x%02x */
	case 0xb6: /* lda $%02x%02x */
	case 0xb7: /* sta $%02x%02x */
	case 0xb8: /* eora $%02x%02x */
	case 0xb9: /* adca $%02x%02x */
	case 0xba: /* ora $%02x%02x */
	case 0xbb: /* adda $%02x%02x */
	case 0xbc: /* cmpx $%02x%02x */
	case 0xbd: /* jsr $%02x%02x */
	case 0xbe: /* ldx $%02x%02x */
	case 0xbf: /* stx $%02x%02x */
	case 0xf0: /* subb $%02x%02x */
	case 0xf1: /* cmpb $%02x%02x */
	case 0xf2: /* sbcb $%02x%02x */
	case 0xf3: /* addd $%02x%02x */
	case 0xf4: /* andb $%02x%02x */
	case 0xf5: /* bitb $%02x%02x */
	case 0xf6: /* ldb $%02x%02x */
	case 0xf7: /* stb $%02x%02x */
	case 0xf8: /* eorb $%02x%02x */
	case 0xf9: /* adcb $%02x%02x */
	case 0xfa: /* orb $%02x%02x */
	case 0xfb: /* addb $%02x%02x */
	case 0xfc: /* ldd $%02x%02x */
	case 0xfd: /* std $%02x%02x */
	case 0xfe: /* ldu $%02x%02x */
	case 0xff: /* stu $%02x%02x */
		entry->num_bytes = 3;
		if (pc + 3 > last_pc) goto truncated;
		op1 = *src++;
		entry->instruction[1] = op1;
		op2 = *src;
		entry->instruction[2] = op2;
		addr = (256 * op1) + op2;
		jmp_targets->discovered[addr] = DISASM_6809;
		entry->target_addr = addr;
		entry->flag = FLAG_TARGET_ADDR;
		entry->disassembler_type = DISASM_6809;
		break;


	/* imm16 */
	case 0x83: /* subd #$%02x%02x */
	case 0x8c: /* cmpx #$%02x%02x */
	case 0x8e: /* ldx #$%02x%02x */
	case 0xc3: /* addd #$%02x%02x */
	case 0xcc: /* ldd #$%02x%02x */
	case 0xce: /* ldu #$%02x%02x */
		entry->num_bytes = 3;
		if (pc + 3 > last_pc) goto truncated;
		op1 = *src++;
		entry->instruction[1] = op1;
		op2 = *src;
		entry->instruction[2] = op2;
		entry->disassembler_type = DISASM_6809;
		break;



	case 0x10:
		opcode = *src++;
		entry->instruction[1] = opcode;
		switch(opcode) {
		/* rel16 */
		case 0x21: /* lbrn $%04x */
		case 0x22: /* lbhi $%04x */
		case 0x23: /* lbls $%04x */
		case 0x24: /* lbhs $%04x */
		case 0x25: /* lblo $%04x */
		case 0x26: /* lbne $%04x */
		case 0x27: /* lbeq $%04x */
		case 0x28: /* lbvc $%04x */
		case 0x29: /* lbvs $%04x */
		case 0x2a: /* lbpl $%04x */
		case 0x2b: /* lbmi $%04x */
		case 0x2c: /* lbge $%04x */
		case 0x2d: /* lblt $%04x */
		case 0x2e: /* lbgt $%04x */
		case 0x2f: /* lble $%04x */
			entry->num_bytes = 4;
			if (pc + 4 > last_pc) goto truncated;
			op1 = *src++;
			entry->instruction[2] = op1;
			op2 = *src;
			entry->instruction[3] = op2;
			addr = op1 + 256 * op2;
			if (addr > 32768) addr -= 0x10000;
			rel = (pc + 2 + addr) & 0xffff;
			jmp_targets->discovered[rel] = DISASM_6809;
			entry->target_addr = rel;
			entry->flag = FLAG_BRANCH_TAKEN;
			entry->disassembler_type = DISASM_6809;
			break;


		/* inherent */
		case 0x3f: /* swi2  */
			entry->num_bytes = 2;
			if (pc + 2 > last_pc) goto truncated;
			entry->disassembler_type = DISASM_6809;
			break;


		/* imm16 */
		case 0x83: /* cmpd #$%02x%02x */
		case 0x8c: /* cmpy #$%02x%02x */
		case 0x8e: /* ldy #$%02x%02x */
		case 0xce: /* lds #$%02x%02x */
			entry->num_bytes = 4;
			if (pc + 4 > last_pc) goto truncated;
			op1 = *src++;
			entry->instruction[2] = op1;
			op2 = *src;
			entry->instruction[3] = op2;
			entry->disassembler_type = DISASM_6809;
			break;


		/* direct */
		case 0x93: /* cmpd $%02x */
		case 0x9c: /* cmpy $%02x */
		case 0x9e: /* ldy $%02x */
		case 0x9f: /* sty $%02x */
		case 0xde: /* lds $%02x */
		case 0xdf: /* sts $%02x */

		/* indexed */
		case 0xa3: /* cmpd $%02x,x */
		case 0xac: /* cmpy $%02x,x */
		case 0xae: /* ldy $%02x,x */
		case 0xaf: /* sty $%02x,x */
		case 0xee: /* lds $%02x,x */
		case 0xef: /* sts $%02x,x */
			entry->num_bytes = 3;
			if (pc + 3 > last_pc) goto truncated;
			op1 = *src;
			entry->instruction[2] = op1;
			jmp_targets->discovered[op1] = DISASM_6809;
			entry->target_addr = op1;
			entry->flag = FLAG_TARGET_ADDR;
			entry->disassembler_type = DISASM_6809;
			break;


		/* extended */
		case 0xb3: /* cmpd $%02x%02x */
		case 0xbc: /* cmpy $%02x%02x */
		case 0xbe: /* ldy $%02x%02x */
		case 0xbf: /* sty $%02x%02x */
		case 0xfe: /* lds $%02x%02x */
		case 0xff: /* sts $%02x%02x */
			entry->num_bytes = 4;
			if (pc + 4 > last_pc) goto truncated;
			op1 = *src++;
			entry->instruction[2] = op1;
			op2 = *src;
			entry->instruction[3] = op2;
			addr = (256 * op1) + op2;
			jmp_targets->discovered[addr] = DISASM_6809;
			entry->target_addr = addr;
			entry->flag = FLAG_TARGET_ADDR;
			entry->disassembler_type = DISASM_6809;
			break;



		default:
			entry->num_bytes = 2;
			goto truncated2;
		}
		break;

	case 0x11:
		opcode = *src++;
		entry->instruction[1] = opcode;
		switch(opcode) {
		/* inherent */
		case 0x3f: /* swi3  */
			entry->num_bytes = 2;
			if (pc + 2 > last_pc) goto truncated;
			entry->disassembler_type = DISASM_6809;
			break;


		/* imm16 */
		case 0x83: /* cmpu #$%02x%02x */
		case 0x8c: /* cmps #$%02x%02x */
			entry->num_bytes = 4;
			if (pc + 4 > last_pc) goto truncated;
			op1 = *src++;
			entry->instruction[2] = op1;
			op2 = *src;
			entry->instruction[3] = op2;
			entry->disassembler_type = DISASM_6809;
			break;


		/* direct */
		case 0x93: /* cmpu $%02x */
		case 0x9c: /* cmps $%02x */

		/* indexed */
		case 0xa3: /* cmpu $%02x,x */
		case 0xac: /* cmps $%02x,x */
			entry->num_bytes = 3;
			if (pc + 3 > last_pc) goto truncated;
			op1 = *src;
			entry->instruction[2] = op1;
			jmp_targets->discovered[op1] = DISASM_6809;
			entry->target_addr = op1;
			entry->flag = FLAG_TARGET_ADDR;
			entry->disassembler_type = DISASM_6809;
			break;


		/* extended */
		case 0xb3: /* cmpu $%02x%02x */
		case 0xbc: /* cmps $%02x%02x */
			entry->num_bytes = 4;
			if (pc + 4 > last_pc) goto truncated;
			op1 = *src++;
			entry->instruction[2] = op1;
			op2 = *src;
			entry->instruction[3] = op2;
			addr = (256 * op1) + op2;
			jmp_targets->discovered[addr] = DISASM_6809;
			entry->target_addr = addr;
			entry->flag = FLAG_TARGET_ADDR;
			entry->disassembler_type = DISASM_6809;
			break;



		default:
			entry->num_bytes = 2;
			goto truncated2;
		}
		break;

	default:
		goto truncated;
	}
	return entry->num_bytes;
truncated:
	entry->num_bytes = 1;
truncated2:
	entry->flag = 0;
	entry->disassembler_type = DISASM_DATA;
	return entry->num_bytes;
}

int parse_entry_6811(history_entry_t *entry, unsigned char *src, unsigned int pc, unsigned int last_pc, jmp_targets_t *jmp_targets) {
	int dist;
	unsigned int rel;
	unsigned short addr;
	unsigned char opcode, op1, op2, op3;
	
	opcode = *src++;
	entry->instruction[0] = opcode;
	entry->pc = (unsigned short)pc;
	entry->target_addr = 0;
	switch(opcode) {
	/* inherent */
	case 0x0: /* test  */
	case 0x1: /* nop  */
	case 0x2: /* idiv  */
	case 0x3: /* fdiv  */
	case 0x4: /* lsrd  */
	case 0x5: /* lsld  */
	case 0x6: /* tap  */
	case 0x7: /* tpa  */
	case 0x8: /* inx  */
	case 0x9: /* dex  */
	case 0xa: /* clv  */
	case 0xb: /* sev  */
	case 0xc: /* clc  */
	case 0xd: /* sec  */
	case 0xe: /* cli  */
	case 0xf: /* sei  */
	case 0x10: /* sba  */
	case 0x11: /* cba  */
	case 0x16: /* tab  */
	case 0x17: /* tba  */
	case 0x19: /* daa  */
	case 0x1b: /* aba  */
	case 0x30: /* tsx  */
	case 0x31: /* ins  */
	case 0x32: /* pula  */
	case 0x33: /* pulb  */
	case 0x34: /* des  */
	case 0x35: /* txs  */
	case 0x36: /* psha  */
	case 0x37: /* pshb  */
	case 0x38: /* pulx  */
	case 0x39: /* rts  */
	case 0x3a: /* abx  */
	case 0x3b: /* rti  */
	case 0x3c: /* pshx  */
	case 0x3d: /* mul  */
	case 0x3e: /* wai  */
	case 0x3f: /* swi  */
	case 0x43: /* coma  */
	case 0x44: /* lsra  */
	case 0x46: /* rora  */
	case 0x47: /* asra  */
	case 0x48: /* lsla  */
	case 0x49: /* rola  */
	case 0x4a: /* deca  */
	case 0x4c: /* inca  */
	case 0x4d: /* tsta  */
	case 0x4f: /* clra  */
	case 0x53: /* comb  */
	case 0x54: /* lsrb  */
	case 0x55: /* rorb  */
	case 0x57: /* asrb  */
	case 0x58: /* lslb  */
	case 0x59: /* rolb  */
	case 0x5a: /* decb  */
	case 0x5c: /* incb  */
	case 0x5d: /* tstb  */
	case 0x5f: /* clrb  */
	case 0x8f: /* xgdx  */
	case 0xcf: /* stop  */
		entry->num_bytes = 1;
		entry->disassembler_type = DISASM_6811;
		break;


	/* direct3 */
	case 0x12: /* brset *$%02x $%02x ${2:04x} */
	case 0x13: /* brclr *$%02x $%02x ${2:04x} */

	/* indexedx3 */
	case 0x1e: /* brset $%02x,x $%02x ${2:04x} */
	case 0x1f: /* brclr $%02x,x $%02x ${2:04x} */
		entry->num_bytes = 4;
		if (pc + 4 > last_pc) goto truncated;
		op1 = *src++;
		entry->instruction[1] = op1;
		op2 = *src++;
		entry->instruction[2] = op2;
		op3 = *src;
		entry->instruction[3] = op3;
		addr = (256 * op1) + op2;
		jmp_targets->discovered[addr] = DISASM_6811;
		entry->target_addr = addr;
		entry->flag = FLAG_BRANCH_TAKEN | FLAG_TARGET_ADDR;
		entry->disassembler_type = DISASM_6811;
		break;


	/* direct2 */
	case 0x14: /* bset *$%02x $%02x */
	case 0x15: /* bclr *$%02x $%02x */

	/* indexedx2 */
	case 0x1c: /* bset $%02x,x $%02x */
	case 0x1d: /* bclr $%02x,x $%02x */

	/* extended */
	case 0x70: /* neg $%02x%02x */
	case 0x73: /* com $%02x%02x */
	case 0x74: /* lsr $%02x%02x */
	case 0x76: /* ror $%02x%02x */
	case 0x77: /* asr $%02x%02x */
	case 0x78: /* lsl $%02x%02x */
	case 0x79: /* rol $%02x%02x */
	case 0x7a: /* dec $%02x%02x */
	case 0x7c: /* inc $%02x%02x */
	case 0x7d: /* tst $%02x%02x */
	case 0x7e: /* jmp $%02x%02x */
	case 0x7f: /* clr $%02x%02x */
	case 0xb0: /* suba $%02x%02x */
	case 0xb1: /* cmpa $%02x%02x */
	case 0xb2: /* sbca $%02x%02x */
	case 0xb3: /* subd $%02x%02x */
	case 0xb4: /* anda $%02x%02x */
	case 0xb5: /* bita $%02x%02x */
	case 0xb6: /* ldaa $%02x%02x */
	case 0xb7: /* staa $%02x%02x */
	case 0xb8: /* eora $%02x%02x */
	case 0xb9: /* adca $%02x%02x */
	case 0xba: /* oraa $%02x%02x */
	case 0xbb: /* adda $%02x%02x */
	case 0xbc: /* cpx $%02x%02x */
	case 0xbd: /* jsr $%02x%02x */
	case 0xbe: /* lds $%02x%02x */
	case 0xbf: /* sts $%02x%02x */
	case 0xf0: /* subb $%02x%02x */
	case 0xf1: /* cmpb $%02x%02x */
	case 0xf2: /* sbcb $%02x%02x */
	case 0xf3: /* addd $%02x%02x */
	case 0xf4: /* andb $%02x%02x */
	case 0xf5: /* bitb $%02x%02x */
	case 0xf6: /* ldab $%02x%02x */
	case 0xf7: /* stab $%02x%02x */
	case 0xf8: /* eorb $%02x%02x */
	case 0xf9: /* adcb $%02x%02x */
	case 0xfa: /* orab $%02x%02x */
	case 0xfb: /* addb $%02x%02x */
	case 0xfc: /* ldd $%02x%02x */
	case 0xfd: /* std $%02x%02x */
	case 0xfe: /* ldx $%02x%02x */
	case 0xff: /* stx $%02x%02x */
		entry->num_bytes = 3;
		if (pc + 3 > last_pc) goto truncated;
		op1 = *src++;
		entry->instruction[1] = op1;
		op2 = *src;
		entry->instruction[2] = op2;
		addr = (256 * op1) + op2;
		jmp_targets->discovered[addr] = DISASM_6811;
		entry->target_addr = addr;
		entry->flag = FLAG_TARGET_ADDR;
		entry->disassembler_type = DISASM_6811;
		break;


	/* relative */
	case 0x20: /* bra $%04x */
	case 0x21: /* brn $%04x */
	case 0x22: /* bhi $%04x */
	case 0x23: /* bls $%04x */
	case 0x24: /* bhs $%04x */
	case 0x25: /* blo $%04x */
	case 0x26: /* bne $%04x */
	case 0x27: /* beq $%04x */
	case 0x28: /* bvc $%04x */
	case 0x29: /* bvs $%04x */
	case 0x2a: /* bpl $%04x */
	case 0x2b: /* bmi $%04x */
	case 0x2c: /* bge $%04x */
	case 0x2d: /* blt $%04x */
	case 0x2e: /* bgt $%04x */
	case 0x2f: /* ble $%04x */
	case 0x8d: /* bsr $%04x */
		entry->num_bytes = 2;
		if (pc + 2 > last_pc) goto truncated;
		op1 = *src;
		entry->instruction[1] = op1;
		if (op1 > 127) dist = op1 - 256; else dist = op1;
		rel = (pc + 2 + dist) & 0xffff;
		jmp_targets->discovered[rel] = DISASM_6811;
		entry->target_addr = rel;
		entry->flag = FLAG_BRANCH_TAKEN;
		entry->disassembler_type = DISASM_6811;
		break;


	/* inherent */
	case 0x40: /* nega  */
	case 0x50: /* negb  */

	/* immediatex */
	case 0x83: /* subd #$%02x%02x */
	case 0x8c: /* cpx #$%02x%02x */
	case 0x8e: /* lds #$%02x%02x */
	case 0xc3: /* addd #$%02x%02x */
	case 0xcc: /* ldd #$%02x%02x */
	case 0xce: /* ldx #$%02x%02x */
		entry->num_bytes = 3;
		if (pc + 3 > last_pc) goto truncated;
		op1 = *src++;
		entry->instruction[1] = op1;
		op2 = *src;
		entry->instruction[2] = op2;
		entry->disassembler_type = DISASM_6811;
		break;


	/* indexedx */
	case 0x60: /* neg $%02x,x */
	case 0x63: /* com $%02x,x */
	case 0x64: /* lsr $%02x,x */
	case 0x66: /* ror $%02x,x */
	case 0x67: /* asr $%02x,x */
	case 0x68: /* lsl $%02x,x */
	case 0x69: /* rol $%02x,x */
	case 0x6a: /* dec $%02x,x */
	case 0x6c: /* inc $%02x,x */
	case 0x6d: /* tst $%02x,x */
	case 0x6e: /* jmp $%02x,x */
	case 0x6f: /* clr $%02x,x */
	case 0xa0: /* suba $%02x,x */
	case 0xa1: /* cmpa $%02x,x */
	case 0xa2: /* sbca $%02x,x */
	case 0xa3: /* subd $%02x,x */
	case 0xa4: /* anda $%02x,x */
	case 0xa5: /* bita $%02x,x */
	case 0xa6: /* ldaa $%02x,x */
	case 0xa7: /* staa $%02x,x */
	case 0xa8: /* eora $%02x,x */
	case 0xa9: /* adca $%02x,x */
	case 0xaa: /* oraa $%02x,x */
	case 0xab: /* adda $%02x,x */
	case 0xac: /* cpx $%02x,x */
	case 0xad: /* jsr $%02x,x */
	case 0xae: /* lds $%02x,x */
	case 0xaf: /* sts $%02x,x */
	case 0xe0: /* subb $%02x,x */
	case 0xe1: /* cmpb $%02x,x */
	case 0xe2: /* sbcb $%02x,x */
	case 0xe3: /* addd $%02x,x */
	case 0xe4: /* andb $%02x,x */
	case 0xe5: /* bitb $%02x,x */
	case 0xe6: /* ldab $%02x,x */
	case 0xe7: /* stab $%02x,x */
	case 0xe8: /* eorb $%02x,x */
	case 0xe9: /* adcb $%02x,x */
	case 0xea: /* orab $%02x,x */
	case 0xeb: /* addb $%02x,x */
	case 0xec: /* ldd $%02x,x */
	case 0xed: /* std $%02x,x */
	case 0xee: /* ldx $%02x,x */
	case 0xef: /* stx $%02x,x */

	/* direct */
	case 0x90: /* suba $%02x */
	case 0x91: /* cmpa $%02x */
	case 0x92: /* sbca $%02x */
	case 0x93: /* subd $%02x */
	case 0x94: /* anda $%02x */
	case 0x95: /* bita $%02x */
	case 0x96: /* ldaa $%02x */
	case 0x97: /* staa $%02x */
	case 0x98: /* eora $%02x */
	case 0x99: /* adca $%02x */
	case 0x9a: /* oraa $%02x */
	case 0x9b: /* adda $%02x */
	case 0x9c: /* cpx $%02x */
	case 0x9d: /* jsr $%02x */
	case 0x9e: /* lds $%02x */
	case 0x9f: /* sts $%02x */
	case 0xd0: /* subb $%02x */
	case 0xd1: /* cmpb $%02x */
	case 0xd2: /* sbcb $%02x */
	case 0xd3: /* addd $%02x */
	case 0xd4: /* andb $%02x */
	case 0xd5: /* bitb $%02x */
	case 0xd6: /* ldab $%02x */
	case 0xd7: /* stab $%02x */
	case 0xd8: /* eorb $%02x */
	case 0xd9: /* adcb $%02x */
	case 0xda: /* orab $%02x */
	case 0xdb: /* addb $%02x */
	case 0xdc: /* ldd $%02x */
	case 0xdd: /* std $%02x */
	case 0xde: /* ldx $%02x */
	case 0xdf: /* stx $%02x */
		entry->num_bytes = 2;
		if (pc + 2 > last_pc) goto truncated;
		op1 = *src;
		entry->instruction[1] = op1;
		jmp_targets->discovered[op1] = DISASM_6811;
		entry->target_addr = op1;
		entry->flag = FLAG_TARGET_ADDR;
		entry->disassembler_type = DISASM_6811;
		break;


	/* immediate */
	case 0x80: /* suba #$%02x */
	case 0x81: /* cmpa #$%02x */
	case 0x82: /* sbca #$%02x */
	case 0x84: /* anda #$%02x */
	case 0x85: /* bita #$%02x */
	case 0x86: /* ldaa #$%02x */
	case 0x88: /* eora #$%02x */
	case 0x89: /* adca #$%02x */
	case 0x8a: /* oraa #$%02x */
	case 0x8b: /* adda #$%02x */
	case 0xc0: /* subb #$%02x */
	case 0xc1: /* cmpb #$%02x */
	case 0xc2: /* sbcb #$%02x */
	case 0xc4: /* andb #$%02x */
	case 0xc5: /* bitb #$%02x */
	case 0xc6: /* ldab #$%02x */
	case 0xc8: /* eorb #$%02x */
	case 0xc9: /* adcb #$%02x */
	case 0xca: /* orab #$%02x */
	case 0xcb: /* addb #$%02x */
		entry->num_bytes = 2;
		if (pc + 2 > last_pc) goto truncated;
		entry->instruction[1] = *src;
		entry->disassembler_type = DISASM_6811;
		break;



	case 0x18:
		opcode = *src++;
		entry->instruction[1] = opcode;
		switch(opcode) {
		/* inherent */
		case 0x8: /* iny  */
		case 0x9: /* dey  */
		case 0x30: /* tsy  */
		case 0x35: /* tys  */
		case 0x38: /* puly  */
		case 0x3a: /* aby  */
		case 0x3c: /* pshy  */
		case 0x8f: /* xgdy  */
			entry->num_bytes = 2;
			if (pc + 2 > last_pc) goto truncated;
			entry->disassembler_type = DISASM_6811;
			break;


		/* indexedy2 */
		case 0x1c: /* bset $%02x,y $%02x */
		case 0x1d: /* bclr $%02x,y $%02x */

		/* extended */
		case 0xbc: /* cpy $%02x%02x */
		case 0xfe: /* ldy $%02x%02x */
		case 0xff: /* sty $%02x%02x */
			entry->num_bytes = 4;
			if (pc + 4 > last_pc) goto truncated;
			op1 = *src++;
			entry->instruction[2] = op1;
			op2 = *src;
			entry->instruction[3] = op2;
			addr = (256 * op1) + op2;
			jmp_targets->discovered[addr] = DISASM_6811;
			entry->target_addr = addr;
			entry->flag = FLAG_TARGET_ADDR;
			entry->disassembler_type = DISASM_6811;
			break;


		/* indexedy3 */
		case 0x1e: /* brset $%02x,y $%02x ${2:04x} */
		case 0x1f: /* brclr $%02x,y $%02x ${2:04x} */
			entry->num_bytes = 5;
			if (pc + 5 > last_pc) goto truncated;
			entry->flag = FLAG_BRANCH_TAKEN | FLAG_TARGET_ADDR;
			entry->disassembler_type = DISASM_6811;
			break;


		/* indexedy */
		case 0x60: /* neg $%02x,y */
		case 0x63: /* com $%02x,y */
		case 0x64: /* lsr $%02x,y */
		case 0x66: /* ror $%02x,y */
		case 0x67: /* asr $%02x,y */
		case 0x68: /* lsl $%02x,y */
		case 0x69: /* rol $%02x,y */
		case 0x6a: /* dec $%02x,y */
		case 0x6c: /* inc $%02x,y */
		case 0x6d: /* tst $%02x,y */
		case 0x6e: /* jmp $%02x,y */
		case 0x7f: /* clr $%02x,y */
		case 0xa0: /* suba $%02x,y */
		case 0xa1: /* cmpa $%02x,y */
		case 0xa2: /* sbca $%02x,y */
		case 0xa3: /* subd $%02x,y */
		case 0xa4: /* anda $%02x,y */
		case 0xa5: /* bita $%02x,y */
		case 0xa6: /* ldaa $%02x,y */
		case 0xa7: /* staa $%02x,y */
		case 0xa8: /* eora $%02x,y */
		case 0xa9: /* adca $%02x,y */
		case 0xaa: /* oraa $%02x,y */
		case 0xab: /* adda $%02x,y */
		case 0xac: /* cpy $%02x,y */
		case 0xad: /* jsr $%02x,y */
		case 0xae: /* lds $%02x,y */
		case 0xaf: /* sts $%02x,y */
		case 0xe0: /* subb $%02x,y */
		case 0xe1: /* cmpb $%02x,y */
		case 0xe2: /* sbcb $%02x,y */
		case 0xe3: /* addd $%02x,y */
		case 0xe4: /* andb $%02x,y */
		case 0xe5: /* bitb $%02x,y */
		case 0xe6: /* ldab $%02x,y */
		case 0xe7: /* stab $%02x,y */
		case 0xe8: /* eorb $%02x,y */
		case 0xe9: /* adcb $%02x,y */
		case 0xea: /* orab $%02x,y */
		case 0xeb: /* addb $%02x,y */
		case 0xec: /* ldd $%02x,y */
		case 0xed: /* std $%02x,y */
		case 0xee: /* ldy $%02x,y */
		case 0xef: /* sty $%02x,y */

		/* direct */
		case 0x9c: /* cpy $%02x */
		case 0xde: /* ldy $%02x */
		case 0xdf: /* sty $%02x */
			entry->num_bytes = 3;
			if (pc + 3 > last_pc) goto truncated;
			op1 = *src;
			entry->instruction[2] = op1;
			jmp_targets->discovered[op1] = DISASM_6811;
			entry->target_addr = op1;
			entry->flag = FLAG_TARGET_ADDR;
			entry->disassembler_type = DISASM_6811;
			break;


		/* immediatex */
		case 0x8c: /* cpy #$%02x%02x */
		case 0xce: /* ldy #$%02x%02x */
			entry->num_bytes = 4;
			if (pc + 4 > last_pc) goto truncated;
			op1 = *src++;
			entry->instruction[2] = op1;
			op2 = *src;
			entry->instruction[3] = op2;
			entry->disassembler_type = DISASM_6811;
			break;



		default:
			entry->num_bytes = 2;
			goto truncated2;
		}
		break;

	case 0x1a:
		opcode = *src++;
		entry->instruction[1] = opcode;
		switch(opcode) {
		/* immediatex */
		case 0x83: /* cpd #$%02x%02x */
			entry->num_bytes = 4;
			if (pc + 4 > last_pc) goto truncated;
			op1 = *src++;
			entry->instruction[2] = op1;
			op2 = *src;
			entry->instruction[3] = op2;
			entry->disassembler_type = DISASM_6811;
			break;


		/* direct */
		case 0x93: /* cpd $%02x */

		/* indexedx */
		case 0xa3: /* cpd $%02x,x */
		case 0xac: /* cpy $%02x,x */
		case 0xee: /* ldy $%02x,x */
		case 0xef: /* sty $%02x,x */
			entry->num_bytes = 3;
			if (pc + 3 > last_pc) goto truncated;
			op1 = *src;
			entry->instruction[2] = op1;
			jmp_targets->discovered[op1] = DISASM_6811;
			entry->target_addr = op1;
			entry->flag = FLAG_TARGET_ADDR;
			entry->disassembler_type = DISASM_6811;
			break;


		/* extended */
		case 0xb3: /* cpd $%02x%02x */
			entry->num_bytes = 4;
			if (pc + 4 > last_pc) goto truncated;
			op1 = *src++;
			entry->instruction[2] = op1;
			op2 = *src;
			entry->instruction[3] = op2;
			addr = (256 * op1) + op2;
			jmp_targets->discovered[addr] = DISASM_6811;
			entry->target_addr = addr;
			entry->flag = FLAG_TARGET_ADDR;
			entry->disassembler_type = DISASM_6811;
			break;



		default:
			entry->num_bytes = 2;
			goto truncated2;
		}
		break;

	case 0xcd:
		opcode = *src++;
		entry->instruction[1] = opcode;
		switch(opcode) {
		/* indexedy */
		case 0xa3: /* cpd $%02x,y */
		case 0xac: /* cpx $%02x,y */
		case 0xee: /* ldx $%02x,y */
		case 0xef: /* stx $%02x,y */
			entry->num_bytes = 3;
			if (pc + 3 > last_pc) goto truncated;
			op1 = *src;
			entry->instruction[2] = op1;
			jmp_targets->discovered[op1] = DISASM_6811;
			entry->target_addr = op1;
			entry->flag = FLAG_TARGET_ADDR;
			entry->disassembler_type = DISASM_6811;
			break;



		default:
			entry->num_bytes = 2;
			goto truncated2;
		}
		break;

	default:
		goto truncated;
	}
	return entry->num_bytes;
truncated:
	entry->num_bytes = 1;
truncated2:
	entry->flag = 0;
	entry->disassembler_type = DISASM_DATA;
	return entry->num_bytes;
}

int parse_entry_8051(history_entry_t *entry, unsigned char *src, unsigned int pc, unsigned int last_pc, jmp_targets_t *jmp_targets) {
	int dist;
	unsigned int rel;
	unsigned short addr;
	unsigned char opcode, op1, op2, op3;
	
	opcode = *src++;
	entry->instruction[0] = opcode;
	entry->pc = (unsigned short)pc;
	entry->target_addr = 0;
	switch(opcode) {
	/*  */
	case 0x0: /* nop  */
	case 0x22: /* ret  */
	case 0x32: /* reti  */

	/* a */
	case 0x3: /* rr a */
	case 0x4: /* inc a */
	case 0x13: /* rrc a */
	case 0x14: /* dec a */
	case 0x23: /* rl a */
	case 0x33: /* rlc a */
	case 0xc4: /* swap a */
	case 0xd4: /* da a */
	case 0xe4: /* clr a */
	case 0xf4: /* cpl a */

	/* @r0 */
	case 0x6: /* inc @r0 */

	/* @r1 */
	case 0x7: /* inc @r1 */
	case 0x17: /* dec @r1 */

	/* r0 */
	case 0x8: /* inc r0 */
	case 0x16: /* dec r0 */
	case 0x18: /* dec r0 */

	/* r1 */
	case 0x9: /* inc r1 */
	case 0x19: /* dec r1 */

	/* r2 */
	case 0xa: /* inc r2 */
	case 0x1a: /* dec r2 */

	/* r3 */
	case 0xb: /* inc r3 */
	case 0x1b: /* dec r3 */

	/* r4 */
	case 0xc: /* inc r4 */
	case 0x1c: /* dec r4 */

	/* r5 */
	case 0xd: /* inc r5 */
	case 0x1d: /* dec r5 */

	/* r6 */
	case 0xe: /* inc r6 */
	case 0x1e: /* dec r6 */

	/* r7 */
	case 0xf: /* inc r7 */
	case 0x1f: /* dec r7 */

	/* a,r0 */
	case 0x26: /* add a,r0 */
	case 0x28: /* add a,r0 */
	case 0x38: /* addc a,r0 */
	case 0x48: /* orl a,r0 */
	case 0x58: /* anl a,r0 */
	case 0x68: /* xrl a,r0 */
	case 0x98: /* subb a,r0 */
	case 0xc8: /* xch a,r0 */
	case 0xe8: /* mov a,r0 */

	/* a,@r1 */
	case 0x27: /* add a,@r1 */
	case 0x37: /* addc a,@r1 */
	case 0x47: /* orl a,@r1 */
	case 0x57: /* anl a,@r1 */
	case 0x67: /* xrl a,@r1 */
	case 0x97: /* subb a,@r1 */
	case 0xc7: /* xch a,@r1 */
	case 0xd7: /* xchd a,@r1 */
	case 0xe3: /* movx a,@r1 */
	case 0xe7: /* mov a,@r1 */

	/* a,r1 */
	case 0x29: /* add a,r1 */
	case 0x39: /* addc a,r1 */
	case 0x49: /* orl a,r1 */
	case 0x59: /* anl a,r1 */
	case 0x69: /* xrl a,r1 */
	case 0x99: /* subb a,r1 */
	case 0xc9: /* xch a,r1 */
	case 0xe9: /* mov a,r1 */

	/* a,r2 */
	case 0x2a: /* add a,r2 */
	case 0x3a: /* addc a,r2 */
	case 0x4a: /* orl a,r2 */
	case 0x5a: /* anl a,r2 */
	case 0x6a: /* xrl a,r2 */
	case 0x9a: /* subb a,r2 */
	case 0xca: /* xch a,r2 */
	case 0xea: /* mov a,r2 */

	/* a,r3 */
	case 0x2b: /* add a,r3 */
	case 0x3b: /* addc a,r3 */
	case 0x4b: /* orl a,r3 */
	case 0x5b: /* anl a,r3 */
	case 0x6b: /* xrl a,r3 */
	case 0x9b: /* subb a,r3 */
	case 0xcb: /* xch a,r3 */
	case 0xeb: /* mov a,r3 */

	/* a,r4 */
	case 0x2c: /* add a,r4 */
	case 0x3c: /* addc a,r4 */
	case 0x4c: /* orl a,r4 */
	case 0x5c: /* anl a,r4 */
	case 0x6c: /* xrl a,r4 */
	case 0x9c: /* subb a,r4 */
	case 0xcc: /* xch a,r4 */
	case 0xec: /* mov a,r4 */

	/* a,r5 */
	case 0x2d: /* add a,r5 */
	case 0x3d: /* addc a,r5 */
	case 0x4d: /* orl a,r5 */
	case 0x5d: /* anl a,r5 */
	case 0x6d: /* xrl a,r5 */
	case 0x9d: /* subb a,r5 */
	case 0xcd: /* xch a,r5 */
	case 0xed: /* mov a,r5 */

	/* a,r6 */
	case 0x2e: /* add a,r6 */
	case 0x3e: /* addc a,r6 */
	case 0x4e: /* orl a,r6 */
	case 0x5e: /* anl a,r6 */
	case 0x6e: /* xrl a,r6 */
	case 0x9e: /* subb a,r6 */
	case 0xce: /* xch a,r6 */
	case 0xee: /* mov a,r6 */

	/* a,r7 */
	case 0x2f: /* add a,r7 */
	case 0x3f: /* addc a,r7 */
	case 0x4f: /* orl a,r7 */
	case 0x5f: /* anl a,r7 */
	case 0x6f: /* xrl a,r7 */
	case 0x9f: /* subb a,r7 */
	case 0xcf: /* xch a,r7 */
	case 0xef: /* mov a,r7 */

	/* a,@r0 */
	case 0x36: /* addc a,@r0 */
	case 0x46: /* orl a,@r0 */
	case 0x56: /* anl a,@r0 */
	case 0x66: /* xrl a,@r0 */
	case 0x96: /* subb a,@r0 */
	case 0xc6: /* xch a,@r0 */
	case 0xd6: /* xchd a,@r0 */
	case 0xe2: /* movx a,@r0 */
	case 0xe6: /* mov a,@r0 */

	/* @a+dptr */
	case 0x73: /* jmp @a+dptr */

	/* a,@a+pc */
	case 0x83: /* movc a,@a+pc */

	/* ab */
	case 0x84: /* div ab */
	case 0xa4: /* mul ab */

	/* a,@a+dptr */
	case 0x93: /* movc a,@a+dptr */

	/* dptr */
	case 0xa3: /* inc dptr */

	/* c */
	case 0xb3: /* cpl c */
	case 0xc3: /* clr c */
	case 0xd3: /* setb c */

	/* a,@dptr */
	case 0xe0: /* movx a,@dptr */

	/* @dptr,a */
	case 0xf0: /* movx @dptr,a */

	/* @r0,a */
	case 0xf2: /* movx @r0,a */
	case 0xf6: /* mov @r0,a */

	/* @r1,a */
	case 0xf3: /* movx @r1,a */
	case 0xf7: /* mov @r1,a */

	/* r0,a */
	case 0xf8: /* mov r0,a */

	/* r1,a */
	case 0xf9: /* mov r1,a */

	/* r2,a */
	case 0xfa: /* mov r2,a */

	/* r3,a */
	case 0xfb: /* mov r3,a */

	/* r4,a */
	case 0xfc: /* mov r4,a */

	/* r5,a */
	case 0xfd: /* mov r5,a */

	/* r6,a */
	case 0xfe: /* mov r6,a */

	/* r7,a */
	case 0xff: /* mov r7,a */
		entry->num_bytes = 1;
		entry->disassembler_type = DISASM_8051;
		break;


	/* addr11 */
	case 0x1: /* ajmp $%02x */
	case 0x11: /* acall $%02x */
	case 0x21: /* ajmp $%02x */
	case 0x31: /* acall $%02x */
	case 0x41: /* ajmp $%02x */
	case 0x51: /* acall $%02x */
	case 0x61: /* ajmp $%02x */
	case 0x71: /* acall $%02x */
	case 0x81: /* ajmp $%02x */
	case 0x91: /* acall $%02x */
	case 0xa1: /* ajmp $%02x */
	case 0xb1: /* acall $%02x */
	case 0xc1: /* ajmp $%02x */
	case 0xd1: /* acall $%02x */
	case 0xe1: /* ajmp $%02x */
	case 0xf1: /* acall $%02x */

	/* direct */
	case 0x5: /* inc $%02x */
	case 0x15: /* dec $%02x */
	case 0xc0: /* push $%02x */
	case 0xd0: /* pop $%02x */

	/* a,immed */
	case 0x24: /* add a,#$%02x */
	case 0x34: /* addc a,#$%02x */
	case 0x44: /* orl a,#$%02x */
	case 0x54: /* anl a,#$%02x */
	case 0x64: /* xrl a,#$%02x */
	case 0x74: /* mov a,#$%02x */
	case 0x94: /* subb a,#$%02x */

	/* a,direct */
	case 0x25: /* add a,$%02x */
	case 0x35: /* addc a,$%02x */
	case 0x45: /* orl a,$%02x */
	case 0x55: /* anl a,$%02x */
	case 0x65: /* xrl a,$%02x */
	case 0x95: /* subb a,$%02x */
	case 0xc5: /* xch a,$%02x */
	case 0xe5: /* mov a,$%02x */

	/* direct,a */
	case 0x42: /* orl $%02x,a */
	case 0x52: /* anl $%02x,a */
	case 0x62: /* xrl $%02x,a */
	case 0xf5: /* mov $%02x,a */

	/* c,bit */
	case 0x72: /* orl c,$%02x */
	case 0x82: /* anl c,$%02x */
	case 0xa0: /* orl c,$%02x */
	case 0xa2: /* mov c,$%02x */
	case 0xb0: /* anl c,$%02x */

	/* @r0,immed */
	case 0x76: /* mov @r0,#$%02x */

	/* @r1,immed */
	case 0x77: /* mov @r1,#$%02x */

	/* r0,immed */
	case 0x78: /* mov r0,#$%02x */

	/* r1,immed */
	case 0x79: /* mov r1,#$%02x */

	/* r2,immed */
	case 0x7a: /* mov r2,#$%02x */

	/* r3,immed */
	case 0x7b: /* mov r3,#$%02x */

	/* r4,immed */
	case 0x7c: /* mov r4,#$%02x */

	/* r5,immed */
	case 0x7d: /* mov r5,#$%02x */

	/* r6,immed */
	case 0x7e: /* mov r6,#$%02x */

	/* r7,immed */
	case 0x7f: /* mov r7,#$%02x */

	/* direct,@r0 */
	case 0x86: /* mov $%02x,@r0 */

	/* direct,@r1 */
	case 0x87: /* mov $%02x,@r1 */

	/* direct,r0 */
	case 0x88: /* mov $%02x,r0 */

	/* direct,r1 */
	case 0x89: /* mov $%02x,r1 */

	/* direct,r2 */
	case 0x8a: /* mov $%02x,r2 */

	/* direct,r3 */
	case 0x8b: /* mov $%02x,r3 */

	/* direct,r4 */
	case 0x8c: /* mov $%02x,r4 */

	/* direct,r5 */
	case 0x8d: /* mov $%02x,r5 */

	/* direct,r6 */
	case 0x8e: /* mov $%02x,r6 */

	/* direct,r7 */
	case 0x8f: /* mov $%02x,r7 */

	/* bit,c */
	case 0x92: /* mov $%02x,c */

	/* @r0,direct */
	case 0xa6: /* mov @r0,$%02x */

	/* @r1,direct */
	case 0xa7: /* mov @r1,$%02x */

	/* r0,direct */
	case 0xa8: /* mov r0,$%02x */

	/* r1,direct */
	case 0xa9: /* mov r1,$%02x */

	/* r2,direct */
	case 0xaa: /* mov r2,$%02x */

	/* r3,direct */
	case 0xab: /* mov r3,$%02x */

	/* r4,direct */
	case 0xac: /* mov r4,$%02x */

	/* r5,direct */
	case 0xad: /* mov r5,$%02x */

	/* r6,direct */
	case 0xae: /* mov r6,$%02x */

	/* r7,direct */
	case 0xaf: /* mov r7,$%02x */

	/* bit */
	case 0xb2: /* cpl $%02x */
	case 0xc2: /* clr $%02x */
	case 0xd2: /* setb $%02x */

	/* r0,offset */
	case 0xd8: /* djnz r0,$%02x */

	/* r1,offset */
	case 0xd9: /* djnz r1,$%02x */

	/* r2,offset */
	case 0xda: /* djnz r2,$%02x */

	/* r3,offset */
	case 0xdb: /* djnz r3,$%02x */

	/* r4,offset */
	case 0xdc: /* djnz r4,$%02x */

	/* r5,offset */
	case 0xdd: /* djnz r5,$%02x */

	/* r6,offset */
	case 0xde: /* djnz r6,$%02x */

	/* r7,offset */
	case 0xdf: /* djnz r7,$%02x */
		entry->num_bytes = 2;
		if (pc + 2 > last_pc) goto truncated;
		entry->instruction[1] = *src;
		entry->disassembler_type = DISASM_8051;
		break;


	/* addr16 */
	case 0x2: /* ljmp $%02x%02x */
	case 0x12: /* lcall $%02x%02x */

	/* bit,offset */
	case 0x10: /* jbc $%02x,$%02x */
	case 0x20: /* jb $%02x,$%02x */
	case 0x30: /* jnb $%02x,$%02x */

	/* direct,immed */
	case 0x43: /* orl $%02x,#$%02x */
	case 0x53: /* anl $%02x,#$%02x */
	case 0x63: /* xrl $%02x,#$%02x */
	case 0x75: /* mov $%02x,#$%02x */

	/* direct,direct */
	case 0x85: /* mov $%02x,$%02x */

	/* dptr,immed */
	case 0x90: /* mov dptr,#$%02x */

	/* a,immed,offset */
	case 0xb4: /* cjne a,#$%02x,$%02x */

	/* a,direct,offset */
	case 0xb5: /* cjne a,$%02x,$%02x */

	/* @r0,immed,offset */
	case 0xb6: /* cjne @r0,#$%02x,$%02x */

	/* @r1,immed,offset */
	case 0xb7: /* cjne @r1,#$%02x,$%02x */

	/* r0,immed,offset */
	case 0xb8: /* cjne r0,#$%02x,$%02x */

	/* r1,immed,offset */
	case 0xb9: /* cjne r1,#$%02x,$%02x */

	/* r2,immed,offset */
	case 0xba: /* cjne r2,#$%02x,$%02x */

	/* r3,immed,offset */
	case 0xbb: /* cjne r3,#$%02x,$%02x */

	/* r4,immed,offset */
	case 0xbc: /* cjne r4,#$%02x,$%02x */

	/* r5,immed,offset */
	case 0xbd: /* cjne r5,#$%02x,$%02x */

	/* r6,immed,offset */
	case 0xbe: /* cjne r6,#$%02x,$%02x */

	/* r7,immed,offset */
	case 0xbf: /* cjne r7,#$%02x,$%02x */

	/* direct,offset */
	case 0xd5: /* djnz $%02x,$%02x */
		entry->num_bytes = 3;
		if (pc + 3 > last_pc) goto truncated;
		op1 = *src++;
		entry->instruction[1] = op1;
		op2 = *src;
		entry->instruction[2] = op2;
		entry->disassembler_type = DISASM_8051;
		break;


	/* offset */
	case 0x40: /* jc $%04x */
	case 0x50: /* jnc $%04x */
	case 0x60: /* jz $%04x */
	case 0x70: /* jnz $%04x */
	case 0x80: /* sjmp $%04x */
		entry->num_bytes = 2;
		if (pc + 2 > last_pc) goto truncated;
		op1 = *src;
		entry->instruction[1] = op1;
		if (op1 > 127) dist = op1 - 256; else dist = op1;
		rel = (pc + 2 + dist) & 0xffff;
		jmp_targets->discovered[rel] = DISASM_8051;
		entry->target_addr = rel;
		entry->flag = FLAG_BRANCH_TAKEN;
		entry->disassembler_type = DISASM_8051;
		break;



	default:
		goto truncated;
	}
	return entry->num_bytes;
truncated:
	entry->num_bytes = 1;
truncated2:
	entry->flag = 0;
	entry->disassembler_type = DISASM_DATA;
	return entry->num_bytes;
}

int parse_entry_8080(history_entry_t *entry, unsigned char *src, unsigned int pc, unsigned int last_pc, jmp_targets_t *jmp_targets) {
	int dist;
	unsigned int rel;
	unsigned short addr;
	unsigned char opcode, op1, op2, op3;
	
	opcode = *src++;
	entry->instruction[0] = opcode;
	entry->pc = (unsigned short)pc;
	entry->target_addr = 0;
	switch(opcode) {
	/* implied */
	case 0x0: /* nop  */
	case 0x7: /* rlc  */
	case 0xf: /* rrc  */
	case 0x17: /* ral  */
	case 0x19: /* dad  */
	case 0x1f: /* rar  */
	case 0x27: /* daa  */
	case 0x2f: /* cma  */
	case 0x37: /* stc  */
	case 0x3f: /* cmc  */
	case 0x76: /* hlt  */
	case 0xc0: /* rnz  */
	case 0xc8: /* rz  */
	case 0xc9: /* ret  */
	case 0xd0: /* rnc  */
	case 0xd8: /* rc  */
	case 0xe0: /* rpo  */
	case 0xe3: /* xthl  */
	case 0xe8: /* rpe  */
	case 0xe9: /* pchl  */
	case 0xeb: /* xchg  */
	case 0xf0: /* rp  */
	case 0xf3: /* di  */
	case 0xf8: /* rm  */
	case 0xf9: /* sphl  */
	case 0xfb: /* ei  */

	/* regb */
	case 0x2: /* stax b */
	case 0x3: /* inx b */
	case 0x4: /* inr b */
	case 0x5: /* dcr b */
	case 0x9: /* dad b */
	case 0xa: /* ldax b */
	case 0xb: /* dcx b */
	case 0x80: /* add b */
	case 0x88: /* adc b */
	case 0x90: /* sub b */
	case 0x98: /* sbb b */
	case 0xa0: /* ana b */
	case 0xa8: /* xra b */
	case 0xb0: /* ora b */
	case 0xb8: /* cmp b */
	case 0xc1: /* pop b */
	case 0xc5: /* push b */

	/* regc */
	case 0xc: /* inr c */
	case 0xd: /* dcr c */
	case 0x81: /* add c */
	case 0x89: /* adc c */
	case 0x91: /* sub c */
	case 0x99: /* sbb c */
	case 0xa1: /* ana c */
	case 0xa9: /* xra c */
	case 0xb1: /* ora c */
	case 0xb9: /* cmp c */

	/* regd */
	case 0x12: /* stax d */
	case 0x13: /* inx d */
	case 0x14: /* inr d */
	case 0x15: /* dcr d */
	case 0x1a: /* ldax d */
	case 0x1b: /* dcx d */
	case 0x82: /* add d */
	case 0x8a: /* adc d */
	case 0x92: /* sub d */
	case 0x9a: /* sbb d */
	case 0xa2: /* ana d */
	case 0xaa: /* xra d */
	case 0xb2: /* ora d */
	case 0xba: /* cmp d */
	case 0xd1: /* pop d */
	case 0xd5: /* push d */

	/* rege */
	case 0x1c: /* inr e */
	case 0x1d: /* dcr e */
	case 0x83: /* add e */
	case 0x8b: /* adc e */
	case 0x93: /* sub e */
	case 0x9b: /* sbb e */
	case 0xa3: /* ana e */
	case 0xab: /* xra e */
	case 0xb3: /* ora e */
	case 0xbb: /* cmp e */

	/* regh */
	case 0x23: /* inx h */
	case 0x24: /* inr h */
	case 0x25: /* dcr h */
	case 0x29: /* dad h */
	case 0x2b: /* dcx h */
	case 0x84: /* add h */
	case 0x8c: /* adc h */
	case 0x94: /* sub h */
	case 0x9c: /* sbb h */
	case 0xa4: /* ana h */
	case 0xac: /* xra h */
	case 0xb4: /* ora h */
	case 0xbc: /* cmp h */
	case 0xe1: /* pop h */
	case 0xe5: /* push h */

	/* regl */
	case 0x2c: /* inr l */
	case 0x2d: /* dcr l */
	case 0x85: /* add l */
	case 0x8d: /* adc l */
	case 0x95: /* sub l */
	case 0x9d: /* sbb l */
	case 0xa5: /* ana l */
	case 0xad: /* xra l */
	case 0xb5: /* ora l */
	case 0xbd: /* cmp l */

	/* regsp */
	case 0x33: /* inx sp */
	case 0x39: /* dad sp */
	case 0x3b: /* dcx sp */

	/* regm */
	case 0x34: /* inr m */
	case 0x35: /* dcr m */
	case 0x86: /* add m */
	case 0x8e: /* adc m */
	case 0x96: /* sub m */
	case 0x9e: /* sbb m */
	case 0xa6: /* ana m */
	case 0xae: /* xra m */
	case 0xb6: /* ora m */
	case 0xbe: /* cmp m */

	/* rega */
	case 0x3c: /* inr a */
	case 0x3d: /* dcr a */
	case 0x87: /* add a */
	case 0x8f: /* adc a */
	case 0x97: /* sub a */
	case 0x9f: /* sbb a */
	case 0xa7: /* ana a */
	case 0xaf: /* xra a */
	case 0xb7: /* ora a */
	case 0xbf: /* cmp a */

	/* regbb */
	case 0x40: /* mov b,b */

	/* regbc */
	case 0x41: /* mov b,c */

	/* regbd */
	case 0x42: /* mov b,d */

	/* regbe */
	case 0x43: /* mov b,e */

	/* regbh */
	case 0x44: /* mov b,h */

	/* regbl */
	case 0x45: /* mov b,l */

	/* regbm */
	case 0x46: /* mov b,m */

	/* regba */
	case 0x47: /* mov b,a */

	/* regcb */
	case 0x48: /* mov c,b */

	/* regcc */
	case 0x49: /* mov c,c */

	/* regcd */
	case 0x4a: /* mov c,d */

	/* regce */
	case 0x4b: /* mov c,e */

	/* regch */
	case 0x4c: /* mov c,h */

	/* regcl */
	case 0x4d: /* mov c,l */

	/* regcm */
	case 0x4e: /* mov c,m */

	/* regca */
	case 0x4f: /* mov c,a */

	/* regdb */
	case 0x50: /* mov d,b */

	/* regdc */
	case 0x51: /* mov d,c */

	/* regdd */
	case 0x52: /* mov d,d */

	/* regde */
	case 0x53: /* mov d,e */

	/* regdh */
	case 0x54: /* mov d,h */

	/* regdl */
	case 0x55: /* mov d,l */

	/* regdm */
	case 0x56: /* mov d,m */

	/* regda */
	case 0x57: /* mov d,a */

	/* regeb */
	case 0x58: /* mov e,b */

	/* regec */
	case 0x59: /* mov e,c */

	/* reged */
	case 0x5a: /* mov e,d */

	/* regee */
	case 0x5b: /* mov e,e */

	/* regeh */
	case 0x5c: /* mov e,h */

	/* regel */
	case 0x5d: /* mov e,l */

	/* regem */
	case 0x5e: /* mov e,m */

	/* regea */
	case 0x5f: /* mov e,a */

	/* reghb */
	case 0x60: /* mov h,b */

	/* reghc */
	case 0x61: /* mov h,c */

	/* reghd */
	case 0x62: /* mov h,d */

	/* reghe */
	case 0x63: /* mov h,e */

	/* reghh */
	case 0x64: /* mov h,h */

	/* reghl */
	case 0x65: /* mov h,l */

	/* reghm */
	case 0x66: /* mov h,m */

	/* regha */
	case 0x67: /* mov h,a */

	/* reglb */
	case 0x68: /* mov l,b */

	/* reglc */
	case 0x69: /* mov l,c */

	/* regld */
	case 0x6a: /* mov l,d */

	/* regle */
	case 0x6b: /* mov l,e */

	/* reglh */
	case 0x6c: /* mov l,h */

	/* regll */
	case 0x6d: /* mov l,l */

	/* reglm */
	case 0x6e: /* mov l,m */

	/* regla */
	case 0x6f: /* mov l,a */

	/* regmb */
	case 0x70: /* mov m,b */

	/* regmc */
	case 0x71: /* mov m,c */

	/* regmd */
	case 0x72: /* mov m,d */

	/* regme */
	case 0x73: /* mov m,e */

	/* regmh */
	case 0x74: /* mov m,h */

	/* regml */
	case 0x75: /* mov m,l */

	/* regma */
	case 0x77: /* mov m,a */

	/* regab */
	case 0x78: /* mov a,b */

	/* regac */
	case 0x79: /* mov a,c */

	/* regad */
	case 0x7a: /* mov a,d */

	/* regae */
	case 0x7b: /* mov a,e */

	/* regah */
	case 0x7c: /* mov a,h */

	/* regal */
	case 0x7d: /* mov a,l */

	/* regam */
	case 0x7e: /* mov a,m */

	/* regaa */
	case 0x7f: /* mov a,a */

	/* 0 */
	case 0xc7: /* rst 0 */

	/* 1 */
	case 0xcf: /* rst 1 */

	/* 2 */
	case 0xd7: /* rst 2 */

	/* 3 */
	case 0xdf: /* rst 3 */

	/* 4 */
	case 0xe7: /* rst 4 */

	/* 5 */
	case 0xef: /* rst 5 */

	/* regpsw */
	case 0xf1: /* pop psw */
	case 0xf5: /* push psw */

	/* 6 */
	case 0xf7: /* rst 6 */

	/* 7 */
	case 0xff: /* rst 7 */
		entry->num_bytes = 1;
		entry->disassembler_type = DISASM_8080;
		break;


	/* immxb */
	case 0x1: /* lxi b,$%02x%02x */

	/* immxd */
	case 0x11: /* lxi d,$%02x%02x */

	/* immxh */
	case 0x21: /* lxi h,$%02x%02x */

	/* immxsp */
	case 0x31: /* lxi sp,$%02x%02x */
		entry->num_bytes = 3;
		if (pc + 3 > last_pc) goto truncated;
		op1 = *src++;
		entry->instruction[1] = op1;
		op2 = *src;
		entry->instruction[2] = op2;
		entry->disassembler_type = DISASM_8080;
		break;


	/* immb */
	case 0x6: /* mvi b,$%02x */

	/* immc */
	case 0xe: /* mvi c,$%02x */

	/* immd */
	case 0x16: /* mvi d,$%02x */

	/* imme */
	case 0x1e: /* mvi e,$%02x */

	/* immh */
	case 0x26: /* mvi h,$%02x */

	/* imml */
	case 0x2e: /* mvi l,$%02x */

	/* immm */
	case 0x36: /* mvi m,$%02x */

	/* imma */
	case 0x3e: /* mvi a,$%02x */

	/* imm */
	case 0xc6: /* adi $%02x */
	case 0xce: /* aci $%02x */
	case 0xd3: /* out $%02x */
	case 0xd6: /* sui $%02x */
	case 0xdb: /* in $%02x */
	case 0xde: /* sbi $%02x */
	case 0xe6: /* ani $%02x */
	case 0xee: /* xri $%02x */
	case 0xf6: /* ori $%02x */
	case 0xfe: /* cpi $%02x */
		entry->num_bytes = 2;
		if (pc + 2 > last_pc) goto truncated;
		entry->instruction[1] = *src;
		entry->disassembler_type = DISASM_8080;
		break;


	/* direct */
	case 0x22: /* shld $%02x%02x */
	case 0x2a: /* lhld $%02x%02x */
	case 0x32: /* sta $%02x%02x */
	case 0x3a: /* lda $%02x%02x */
	case 0xc2: /* jnz $%02x%02x */
	case 0xc3: /* jmp $%02x%02x */
	case 0xc4: /* cnz $%02x%02x */
	case 0xca: /* jz $%02x%02x */
	case 0xcc: /* cz $%02x%02x */
	case 0xcd: /* call $%02x%02x */
	case 0xd2: /* jnc $%02x%02x */
	case 0xd4: /* cnc $%02x%02x */
	case 0xda: /* jc $%02x%02x */
	case 0xdc: /* cc $%02x%02x */
	case 0xe2: /* jpo $%02x%02x */
	case 0xe4: /* cpo $%02x%02x */
	case 0xea: /* jpe $%02x%02x */
	case 0xec: /* cpe $%02x%02x */
	case 0xf2: /* jp $%02x%02x */
	case 0xf4: /* cp $%02x%02x */
	case 0xfa: /* jm $%02x%02x */
	case 0xfc: /* cm $%02x%02x */
		entry->num_bytes = 3;
		if (pc + 3 > last_pc) goto truncated;
		op1 = *src++;
		entry->instruction[1] = op1;
		op2 = *src;
		entry->instruction[2] = op2;
		addr = (256 * op2) + op1;
		jmp_targets->discovered[addr] = DISASM_8080;
		entry->target_addr = addr;
		entry->flag = FLAG_TARGET_ADDR;
		entry->disassembler_type = DISASM_8080;
		break;



	default:
		goto truncated;
	}
	return entry->num_bytes;
truncated:
	entry->num_bytes = 1;
truncated2:
	entry->flag = 0;
	entry->disassembler_type = DISASM_DATA;
	return entry->num_bytes;
}

int parse_entry_jumpman_level(history_entry_t *entry, unsigned char *src, unsigned int pc, unsigned int last_pc, jmp_targets_t *jmp_targets) {
	int dist;
	unsigned int rel;
	unsigned short addr;
	unsigned char opcode, op1, op2, op3;
	
	opcode = *src++;
	entry->instruction[0] = opcode;
	entry->pc = (unsigned short)pc;
	entry->target_addr = 0;
	switch(opcode) {
	/* type */
	case 0xfc: /* type $%02x%02x */

	/* spacing */
	case 0xfe: /* spacing dx=$%02x dy=$%02x */
		entry->num_bytes = 3;
		if (pc + 3 > last_pc) goto truncated;
		op1 = *src++;
		entry->instruction[1] = op1;
		op2 = *src;
		entry->instruction[2] = op2;
		entry->disassembler_type = DISASM_JUMPMAN_LEVEL;
		break;


	/* draw */
	case 0xfd: /* draw x=$%02x y=$%02x len=$%02x */
		entry->num_bytes = 4;
		if (pc + 4 > last_pc) goto truncated;
		op1 = *src++;
		entry->instruction[1] = op1;
		op2 = *src++;
		entry->instruction[2] = op2;
		op3 = *src;
		entry->instruction[3] = op3;
		entry->disassembler_type = DISASM_JUMPMAN_LEVEL;
		break;


	/* implicit */
	case 0xff: /* end  */
		entry->num_bytes = 1;
		entry->disassembler_type = DISASM_JUMPMAN_LEVEL;
		break;



	default:
		goto truncated;
	}
	return entry->num_bytes;
truncated:
	entry->num_bytes = 1;
truncated2:
	entry->flag = 0;
	entry->disassembler_type = DISASM_DATA;
	return entry->num_bytes;
}


extern int parse_entry_data(history_entry_t *entry, unsigned char *src, unsigned int pc, unsigned int last_pc, jmp_targets_t *jmp_targets);
extern int parse_entry_antic_dl(history_entry_t *entry, unsigned char *src, unsigned int pc, unsigned int last_pc, jmp_targets_t *jmp_targets);
extern int parse_entry_jumpman_harvest(history_entry_t *entry, unsigned char *src, unsigned int pc, unsigned int last_pc, jmp_targets_t *jmp_targets);

void *parser_map[] = {
parse_entry_data, /* 0 */
parse_entry_data, /* 1 */
parse_entry_data, /* 2 */
parse_entry_data, /* 3 */
parse_entry_data, /* 4 */
parse_entry_data, /* 5 */
parse_entry_data, /* 6 */
parse_entry_data, /* 7 */
parse_entry_data, /* 8 */
parse_entry_data, /* 9 */
parse_entry_6502, /* 10 */
parse_entry_6502undoc, /* 11 */
parse_entry_65816, /* 12 */
parse_entry_65c02, /* 13 */
parse_entry_6800, /* 14 */
parse_entry_6809, /* 15 */
parse_entry_6811, /* 16 */
parse_entry_8051, /* 17 */
parse_entry_8080, /* 18 */
parse_entry_data, /* 19 */
parse_entry_data, /* 20 */
parse_entry_data, /* 21 */
parse_entry_data, /* 22 */
parse_entry_data, /* 23 */
parse_entry_data, /* 24 */
parse_entry_data, /* 25 */
parse_entry_data, /* 26 */
parse_entry_data, /* 27 */
parse_entry_data, /* 28 */
parse_entry_data, /* 29 */
parse_entry_antic_dl, /* 30 */
parse_entry_jumpman_harvest, /* 31 */
parse_entry_jumpman_level, /* 32 */
parse_entry_data, /* 33 */
parse_entry_data, /* 34 */
parse_entry_data, /* 35 */
parse_entry_data, /* 36 */
parse_entry_data, /* 37 */
parse_entry_data, /* 38 */
parse_entry_data, /* 39 */
parse_entry_data, /* 40 */
parse_entry_data, /* 41 */
parse_entry_data, /* 42 */
parse_entry_data, /* 43 */
parse_entry_data, /* 44 */
parse_entry_data, /* 45 */
parse_entry_data, /* 46 */
parse_entry_data, /* 47 */
parse_entry_data, /* 48 */
parse_entry_data, /* 49 */
parse_entry_data, /* 50 */
parse_entry_data, /* 51 */
parse_entry_data, /* 52 */
parse_entry_data, /* 53 */
parse_entry_data, /* 54 */
parse_entry_data, /* 55 */
parse_entry_data, /* 56 */
parse_entry_data, /* 57 */
parse_entry_data, /* 58 */
parse_entry_data, /* 59 */
parse_entry_data, /* 60 */
parse_entry_data, /* 61 */
parse_entry_data, /* 62 */
parse_entry_data, /* 63 */
parse_entry_data, /* 64 */
parse_entry_data, /* 65 */
parse_entry_data, /* 66 */
parse_entry_data, /* 67 */
parse_entry_data, /* 68 */
parse_entry_data, /* 69 */
parse_entry_data, /* 70 */
parse_entry_data, /* 71 */
parse_entry_data, /* 72 */
parse_entry_data, /* 73 */
parse_entry_data, /* 74 */
parse_entry_data, /* 75 */
parse_entry_data, /* 76 */
parse_entry_data, /* 77 */
parse_entry_data, /* 78 */
parse_entry_data, /* 79 */
parse_entry_data, /* 80 */
parse_entry_data, /* 81 */
parse_entry_data, /* 82 */
parse_entry_data, /* 83 */
parse_entry_data, /* 84 */
parse_entry_data, /* 85 */
parse_entry_data, /* 86 */
parse_entry_data, /* 87 */
parse_entry_data, /* 88 */
parse_entry_data, /* 89 */
parse_entry_data, /* 90 */
parse_entry_data, /* 91 */
parse_entry_data, /* 92 */
parse_entry_data, /* 93 */
parse_entry_data, /* 94 */
parse_entry_data, /* 95 */
parse_entry_data, /* 96 */
parse_entry_data, /* 97 */
parse_entry_data, /* 98 */
parse_entry_data, /* 99 */
parse_entry_data, /* 100 */
parse_entry_data, /* 101 */
parse_entry_data, /* 102 */
parse_entry_data, /* 103 */
parse_entry_data, /* 104 */
parse_entry_data, /* 105 */
parse_entry_data, /* 106 */
parse_entry_data, /* 107 */
parse_entry_data, /* 108 */
parse_entry_data, /* 109 */
parse_entry_data, /* 110 */
parse_entry_data, /* 111 */
parse_entry_data, /* 112 */
parse_entry_data, /* 113 */
parse_entry_data, /* 114 */
parse_entry_data, /* 115 */
parse_entry_data, /* 116 */
parse_entry_data, /* 117 */
parse_entry_data, /* 118 */
parse_entry_data, /* 119 */
parse_entry_data, /* 120 */
parse_entry_data, /* 121 */
parse_entry_data, /* 122 */
parse_entry_data, /* 123 */
parse_entry_data, /* 124 */
parse_entry_data, /* 125 */
parse_entry_data, /* 126 */
parse_entry_data, /* 127 */
parse_entry_data, /* 128 */
parse_entry_data, /* 129 */
parse_entry_data, /* 130 */
parse_entry_data, /* 131 */
parse_entry_data, /* 132 */
parse_entry_data, /* 133 */
parse_entry_data, /* 134 */
parse_entry_data, /* 135 */
parse_entry_data, /* 136 */
parse_entry_data, /* 137 */
parse_entry_data, /* 138 */
parse_entry_data, /* 139 */
parse_entry_data, /* 140 */
parse_entry_data, /* 141 */
parse_entry_data, /* 142 */
parse_entry_data, /* 143 */
parse_entry_data, /* 144 */
parse_entry_data, /* 145 */
parse_entry_data, /* 146 */
parse_entry_data, /* 147 */
parse_entry_data, /* 148 */
parse_entry_data, /* 149 */
parse_entry_data, /* 150 */
parse_entry_data, /* 151 */
parse_entry_data, /* 152 */
parse_entry_data, /* 153 */
parse_entry_data, /* 154 */
parse_entry_data, /* 155 */
parse_entry_data, /* 156 */
parse_entry_data, /* 157 */
parse_entry_data, /* 158 */
parse_entry_data, /* 159 */
parse_entry_data, /* 160 */
parse_entry_data, /* 161 */
parse_entry_data, /* 162 */
parse_entry_data, /* 163 */
parse_entry_data, /* 164 */
parse_entry_data, /* 165 */
parse_entry_data, /* 166 */
parse_entry_data, /* 167 */
parse_entry_data, /* 168 */
parse_entry_data, /* 169 */
parse_entry_data, /* 170 */
parse_entry_data, /* 171 */
parse_entry_data, /* 172 */
parse_entry_data, /* 173 */
parse_entry_data, /* 174 */
parse_entry_data, /* 175 */
parse_entry_data, /* 176 */
parse_entry_data, /* 177 */
parse_entry_data, /* 178 */
parse_entry_data, /* 179 */
parse_entry_data, /* 180 */
parse_entry_data, /* 181 */
parse_entry_data, /* 182 */
parse_entry_data, /* 183 */
parse_entry_data, /* 184 */
parse_entry_data, /* 185 */
parse_entry_data, /* 186 */
parse_entry_data, /* 187 */
parse_entry_data, /* 188 */
parse_entry_data, /* 189 */
parse_entry_data, /* 190 */
parse_entry_data, /* 191 */
parse_entry_data, /* 192 */
parse_entry_data, /* 193 */
parse_entry_data, /* 194 */
parse_entry_data, /* 195 */
parse_entry_data, /* 196 */
parse_entry_data, /* 197 */
parse_entry_data, /* 198 */
parse_entry_data, /* 199 */
parse_entry_data, /* 200 */
parse_entry_data, /* 201 */
parse_entry_data, /* 202 */
parse_entry_data, /* 203 */
parse_entry_data, /* 204 */
parse_entry_data, /* 205 */
parse_entry_data, /* 206 */
parse_entry_data, /* 207 */
parse_entry_data, /* 208 */
parse_entry_data, /* 209 */
parse_entry_data, /* 210 */
parse_entry_data, /* 211 */
parse_entry_data, /* 212 */
parse_entry_data, /* 213 */
parse_entry_data, /* 214 */
parse_entry_data, /* 215 */
parse_entry_data, /* 216 */
parse_entry_data, /* 217 */
parse_entry_data, /* 218 */
parse_entry_data, /* 219 */
parse_entry_data, /* 220 */
parse_entry_data, /* 221 */
parse_entry_data, /* 222 */
parse_entry_data, /* 223 */
parse_entry_data, /* 224 */
parse_entry_data, /* 225 */
parse_entry_data, /* 226 */
parse_entry_data, /* 227 */
parse_entry_data, /* 228 */
parse_entry_data, /* 229 */
parse_entry_data, /* 230 */
parse_entry_data, /* 231 */
parse_entry_data, /* 232 */
parse_entry_data, /* 233 */
parse_entry_data, /* 234 */
parse_entry_data, /* 235 */
parse_entry_data, /* 236 */
parse_entry_data, /* 237 */
parse_entry_data, /* 238 */
parse_entry_data, /* 239 */
parse_entry_data, /* 240 */
parse_entry_data, /* 241 */
parse_entry_data, /* 242 */
parse_entry_data, /* 243 */
parse_entry_data, /* 244 */
parse_entry_data, /* 245 */
parse_entry_data, /* 246 */
parse_entry_data, /* 247 */
parse_entry_data, /* 248 */
parse_entry_data, /* 249 */
parse_entry_data, /* 250 */
parse_entry_data, /* 251 */
parse_entry_data, /* 252 */
parse_entry_data, /* 253 */
parse_entry_data, /* 254 */
parse_entry_data, /* 255 */
};

load immediate:
	li	register_destination, value
# load immediate value into destination register

subroutine call: "jump and link" instruction

	jal	sub_label	#  "jump and link"
# copy program counter (return address) to register $ra (return address register)
# jump to program statement at sub_label

	move	$a0, $t2	
  # move integer to be printed into $a0:  $a0 = $t2

  add	$t1,$t1,$t3		
  # $t1 = $t1 + $t3

  addi	$t0, 1			
  # increment counter
  
  bgt	$t0,$t1,target		
  #  branch to target if  $t0 > $t1
      ex:
        bgt $t1, 0, inc_loop # repeat if $t1 is greater than 0


	
  jr	$t3		#  jump to address contained in $t3 ("jump register")

 32 general-purpose registers
register preceded by $ in assembly language instruction
two formats for addressing:
using register number ex $0 through $31
using equivalent names ex $t1, $sp
register use conventions
$t0 - $t9 ( = $8 - $15, $24, $25) are general use registers; need not be preserved across procedure calls
$s0 - $s7 ( = $16 - $23) are general use registers; should be preserved across procedure calls
$sp ( = $29) is stack pointer
$fp ( = $30) is frame pointer
$ra ( = $31) is return address storage for subroutine call
$a0 - $a3 ( = $4 - $7) are used to pass arguments to subroutines
$v0, $v1 ( = $2, $3) are used to hold return values from subroutine
special registers Lo and Hi used to store result of multiplication and division
not directly addressable; contents accessed with special instruction mfhi ("move from Hi") and mflo ("move from Lo")
stack grows from high memory to low memory




How to use SYSCALL system services
Step 1. Load the service number in register $v0.
Step 2. Load argument values, if any, in $a0, $a1, $a2, or $f12 as specified.
Step 3. Issue the SYSCALL instruction.
Step 4. Retrieve return values, if any, from result registers as specified.

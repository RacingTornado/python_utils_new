/* '3.3.1 Clock Data Bytes Out on +ve clock edge MSB first (no read)';
*/
void func_CLOCK_BYTES_OUT_POS_MSB()
{
}
/* '3.3.2 Clock Data Bytes Out on -ve clock edge MSB first (no read)';
*/
void func_CLOCK_BYTES_OUT_NEG_MSB()
{
}
/* '3.3.3 Clock Data Bits Out on +ve clock edge MSB first (no read)';
*/
void func_CLOCK_BITS_OUT_POS_MSB()
{
}
/* '3.3.4 Clock Data Bits Out on -ve clock edge MSB first (no read)';
*/
void func_CLOCK_BITS_OUT_NEG_MSB()
{
}
/* '3.3.5 Clock Data Bytes In on +ve clock edge MSB first (no write)';
*/
void func_CLOCK_BYTES_IN_POS_MSB()
{
}
/* '3.3.6 Clock Data Bytes In on -ve clock edge MSB first (no write)';
*/
void func_CLOCK_BYTES_IN_NEG_MSB()
{
}
/* '3.3.7 Clock Data Bits In on +ve clock edge MSB first (no write)';
*/
void func_CLOCK_BITS_IN_POS_MSB()
{
}
/* '3.3.8 Clock Data Bits In on -ve clock edge MSB first (no write)';
*/
void func_CLOCK_BITS_IN_NEG_MSB()
{
}
/* '3.3.9 Clock Data Bytes In and Out MSB first,edged';
*/
void func_CLOCK_BYTES_IN_OUT_NORMAL_MSB()
{
}
/* '3.3.9 Clock Data Bytes In and Out MSB first,edged';
*/
void func_CLOCK_BYTES_IN_OUT_INVERTED_MSB()
{
}
/* '3.3.10 Clock Data bits In and Out MSB first';
*/
void func_CLOCK_BITS_IN_OUT_NORMAL_MSB()
{
}
/* '3.3.10 Clock Data bits In and Out MSB first,edged';
*/
void func_CLOCK_BITS_IN_OUT_INVERTED_MSB()
{
}
/* '3.4.1 Clock Data Bytes Out on +ve clock edge LSB first (no read)';
*/
void func_CLOCK_BYTES_OUT_POS_LSB()
{
}
/* '3.4.2 Clock Data Bytes Out on -ve clock edge LSB first (no read)';
*/
void func_CLOCK_BYTES_OUT_NEG_LSB()
{
}
/* '3.4.3 Clock Data Bits Out on +ve clock edge LSB first (no read)';
*/
void func_CLOCK_BITS_OUT_POS_LSB()
{
}
/* '3.4.4 Clock Data Bits Out on -ve clock edge LSB first (no read)';
*/
void func_CLOCK_BITS_OUT_NEG_LSB()
{
}
/* '3.4.5 Clock Data Bytes In on +ve clock edge LSB first (no write)';
*/
void func_CLOCK_BYTES_IN_POS_LSB()
{
}
/* '3.4.6 Clock Data Bytes In on -ve clock edge LSB first (no write)';
*/
void func_CLOCK_BYTES_IN_NEG_LSB()
{
}
/* '3.4.7 Clock Data Bits In on +ve clock edge LSB first (no write)';
*/
void func_CLOCK_BITS_IN_POS_LSB()
{
}
/* '3.4.8 Clock Data Bits In on -ve clock edge LSB first (no write)';
*/
void func_CLOCK_BITS_IN_NEG_LSB()
{
}
/* '3.4.9 Clock Data Bytes In and Out LSB first,edged';
*/
void func_CLOCK_BYTES_IN_OUT_NORMAL_LSB()
{
}
/* '3.4.9 Clock Data Bytes In and Out LSB first,edged';
*/
void func_CLOCK_BYTES_IN_OUT_INVERTED_LSB()
{
}
/* '3.4.10 Clock Data Bits In and Out LSB first,edged';
*/
void func_CLOCK_BITS_IN_OUT_NORMAL_LSB()
{
}
/* '3.4.10 Clock Data Bits In and Out LSB first,edged';
*/
void func_CLOCK_BITS_IN_OUT_INVERTED_LSB()
{
}
/* '3.5.1 Clock Data to TMS pin (no read)';
*/
void func_CLOCK_DATA_TMS_POS()
{
}
/* '3.5.1 Clock Data to TMS pin (no read)';
*/
void func_CLOCK_DATA_TMS_NEG()
{
}
/* '3.5.2 Clock Data to TMS pin with read';
*/
void func_TMS_READ_POS_POS()
{
}
/* '3.5.2 Clock Data to TMS pin with read';
*/
void func_TMS_READ_NEG_POS()
{
}
/* '3.5.2 Clock Data to TMS pin with read';
*/
void func_TMS_READ_POS_NEG()
{
}
/* '3.5.2 Clock Data to TMS pin with read';
*/
void func_TMS_READ_NEG_NEG()
{
}
/* '3.6.1 Set Data bits LowByte';
*/
void func_SET_BITS_LOW()
{
}
/* '3.6.2 Set Data bits High Byte';
*/
void func_SET_BITS_HIGH()
{
}
/* '3.6.3 Read Data bits LowByte';
*/
void func_GET_BITS_LOW()
{
}
/* '3.6.4 Read Data bits HighByte';
*/
void func_GET_BITS_HIGH()
{
}
/* '3.7.1 Connect TDI to TDO for Loopback';
*/
void func_LOOPBACK_START()
{
}
/* '3.7.2 Disconnect TDI to TDO for Loopback';
*/
void func_LOOPBACK_END()
{
}
/* '3.8.1 Set TCK/SK Divisor (FT2232D)';
*/
void func_TCK_DIVISOR()
{
}
/* 'Flush buffer';
*/
void func_SEND_IMMEDIATE()
{
}
/* '5.2 Wait On I/O High';
*/
void func_WAIT_ON_HIGH()
{
}
/* '5.3 Wait On I/O Low';
*/
void func_WAIT_ON_LOW()
{
}
/* 'Disables the clk divide by 5 to allow for a 60MHz master clock. ';
*/
void func_DIS_DIV_5()
{
}
/* 'Enables the clk divide by 5 to allow for backward compatibility with FT2232D';
*/
void func_EN_DIV_5()
{
}
/* 'Enables 3 phase data clocking. Used by I2C interfaces to allow data on both clock edges.';
*/
void func_EN_3_PHASE()
{
}
/* 'Disables 3 phase data clocking.';
*/
void func_DIS_3_PHASE()
{
}
/* 'Allows for a clock to be output without transferring data. Commonly used in the JTAG state machine. Clocks counted in terms of numbers of bits';
*/
void func_CLK_BITS()
{
}
/* 'Allows for a clock to be output without transferring data. Commonly used in the JTAG state machine. Clocks counted in terms of numbers of bytes';
*/
void func_CLK_BYTES()
{
}
/* 'Allows for a clock to be output without transferring datauntil a logic 1 input on GPIOL1stops the clock.';
*/
void func_CLK_WAIT_HIGH()
{
}
/* 'Allows for a clock to be output without transferring datauntil a logic 0 input on GPIOL1stops the clock.';
*/
void func_CLK_WAIT_LOW()
{
}
/* 'Enable adaptive clocking';
*/
void func_EN_ADAPTIVE()
{
}
/* 'Disable adaptive clocking';
*/
void func_DIS_ADAPTIVE()
{
}
/* 'Allows for a clock to be output without transferring data until a logic1 input on GPIOL1stops the clock or a set number of clock pulses are sent. Clocks counted in terms of numbers of bytes';
*/
void func_CLK_BYTES_OR_HIGH()
{
}
/* 'Allows for a clock to be output without transferring datauntil a logic 0 input on GPIOL1stops the clock or a set number of clock pulses are sent. Clocks counted in terms of numbers of bytes';
*/
void func_CLK_BYTES_OR_LOW()
{
}

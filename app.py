from dash import Dash, dash_table, dcc, html, Input, Output, callback
import pandas as pd
import dash_bootstrap_components as dbc
import plotly.express as px
from datetime import datetime
import plotly.graph_objects as go
df_grp_dash=pd.read_csv('pie_states_dash.csv')
df_table = pd.read_csv('css_states_dash.csv')
df_states = pd.read_csv('css_states.csv')
df_time_lg = pd.read_csv('time.csv')

sram_df_grp_dash=pd.read_csv('sram_pie_states_dash.csv')
sram_df_table = pd.read_csv('sram_css_states_dash.csv')
sram_df_states = pd.read_csv('sram_css_states.csv')
sram_df_time_lg = pd.read_csv('sram_time.csv')

fcb_df_grp_dash=pd.read_csv('fcb_pie_states_dash.csv')
fcb_df_table = pd.read_csv('fcb_css_states_dash.csv')
fcb_df_states = pd.read_csv('fcb_css_states.csv')
fcb_df_time_lg = pd.read_csv('fcb_time.csv')


##testinG##
time_var= df_time_lg["Regression_Run_Time"]
print(time_var)

df_f = pd.read_csv('css_states.csv')
df_f = df_f[['Sr#','IP', 'Test_Name', 'Status', 'Remarks']]

sram_df_f = pd.read_csv('sram_css_states.csv')
sram_df_f = sram_df_f[['Test_Name', 'Status', 'Remarks']]

fcb_df_f = pd.read_csv('fcb_css_states.csv')
fcb_df_f = fcb_df_f[['Test_Name', 'Status', 'Remarks']]
####Percentage Section##
df_pcnt = pd.DataFrame(columns = ["IP","Total_Tests","Tests_Passed","Tests_Failed","Timeout","Percentage"])


passed_uart0=len(df_f[df_f['Status'].str.contains('Passed') & df_f['IP'].str.contains('UART0') ])
failed_uart0=len(df_f[df_f['Status'].str.contains('Failed') & df_f['IP'].str.contains('UART0') ])
timeout_uart0=len(df_f[df_f['Status'].str.contains('timeout') & df_f['IP'].str.contains('UART0')])

grand_total_passed=passed_uart0
#print("UART0 Total Passed",passed_uart0)
grand_total_failed=failed_uart0
#print("UART0 Total Failed",failed_uart0)
grand_total_timeout=timeout_uart0
#print("UART0 Total Timeout",timeout_uart0)
sub_total=int(passed_uart0+failed_uart0+timeout_uart0)
print(sub_total)
percentage_uart0=(passed_uart0/sub_total)*100

#print("UART0 Pass Percentage",int(percentage_uart0))
df_pcnt= df_pcnt.append({'IP' : 'UART0', 'Total_Tests' : sub_total , 'Tests_Passed' : int(passed_uart0) , 'Tests_Failed': int(failed_uart0), 'Timeout' : int(timeout_uart0), 'Percentage' : int(percentage_uart0)},
        ignore_index = True)

#print(df_pcnt)

passed_uart1=len(df_f[df_f['Status'].str.contains('Passed') & df_f['IP'].str.contains('UART1') ])
failed_uart1=len(df_f[df_f['Status'].str.contains('Failed') & df_f['IP'].str.contains('UART1') ])
timeout_uart1=len(df_f[df_f['Status'].str.contains('timeout') & df_f['IP'].str.contains('UART1')])

grand_total_passed=passed_uart1+grand_total_passed
#print("UART1 Total Passed",passed_uart1)
grand_total_failed=failed_uart1+grand_total_failed
#print("UART1 Total Failed",failed_uart1)
grand_total_timeout=timeout_uart1+grand_total_timeout
#print("UART1 Total Timeout",timeout_uart1)
sub_total=passed_uart1+failed_uart1+timeout_uart1
percentage_uart1=(passed_uart1/sub_total)*100


df_pcnt= df_pcnt.append({'IP' : 'UART1', 'Total_Tests' : sub_total , 'Tests_Passed' : int(passed_uart1) , 'Tests_Failed': int(failed_uart1), 'Timeout' : int(timeout_uart1), 'Percentage' : int(percentage_uart1)},
        ignore_index = True)

#print(df_pcnt)
#print("UART1 Pass Percentage",int(percentage_uart1))

passed_i2c=len(df_f[df_f['Status'].str.contains('Passed') & df_f['IP'].str.contains('I2C') ])
failed_i2c=len(df_f[df_f['Status'].str.contains('Failed') & df_f['IP'].str.contains('I2C') ])
timeout_i2c=len(df_f[df_f['Status'].str.contains('timeout') & df_f['IP'].str.contains('I2C')])

grand_total_passed=passed_i2c+grand_total_passed
#print("I2C Total Passed",passed_i2c)
grand_total_failed=failed_i2c+grand_total_failed
#print("I2C Total Failed",failed_i2c)
grand_total_timeout=timeout_i2c+grand_total_timeout
#print("I2C Total Timeout",timeout_i2c)
sub_total=passed_i2c+failed_i2c+timeout_i2c
percentage_i2c=(passed_i2c/sub_total)*100

df_pcnt= df_pcnt.append({'IP' : 'I2C', 'Total_Tests' : sub_total , 'Tests_Passed' : int(passed_i2c) , 'Tests_Failed': int(failed_i2c), 'Timeout' : int(timeout_i2c), 'Percentage' : int(percentage_i2c)},
        ignore_index = True)

# print(df_pcnt)
#print("I2C Pass Percentage",int(percentage_i2c))

passed_spi=len(df_f[df_f['Status'].str.contains('Passed') & df_f['IP'].str.contains('SPI') ])
failed_spi=len(df_f[df_f['Status'].str.contains('Failed') & df_f['IP'].str.contains('SPI') ])
timeout_spi=len(df_f[df_f['Status'].str.contains('timeout') & df_f['IP'].str.contains('SPI')])

grand_total_passed=passed_spi+grand_total_passed
#print("SPI Total Passed",passed_spi)
grand_total_failed=failed_spi+grand_total_failed
#print("SPI Total Failed",failed_spi)
grand_total_timeout=timeout_spi+grand_total_timeout
#print("SPI Total Timeout",timeout_spi)
sub_total=passed_spi+failed_spi+timeout_spi
percentage_spi=(passed_spi/sub_total)*100

df_pcnt= df_pcnt.append({'IP' : 'SPI', 'Total_Tests' : sub_total , 'Tests_Passed' : int(passed_spi) , 'Tests_Failed': int(failed_spi), 'Timeout' : int(timeout_spi), 'Percentage' : int(percentage_spi)},
        ignore_index = True)

# print(df_pcnt)
#print("SPI Pass Percentage",int(percentage_spi))

passed_dma=len(df_f[df_f['Status'].str.contains('Passed') & df_f['IP'].str.contains('DMA') ])
failed_dma=len(df_f[df_f['Status'].str.contains('Failed') & df_f['IP'].str.contains('DMA') ])
timeout_dma=len(df_f[df_f['Status'].str.contains('timeout') & df_f['IP'].str.contains('DMA')])

grand_total_passed=passed_dma+grand_total_passed
#print("DMA Total Passed",passed_dma)
grand_total_failed=failed_dma+grand_total_failed
#print("DMA Total Failed",failed_dma)
grand_total_timeout=timeout_dma+grand_total_timeout
#print("DMA Total Timeout",timeout_dma)
sub_total=passed_dma+failed_dma+timeout_dma
percentage_dma=(passed_dma/sub_total)*100

#print("DMA Pass Percentage",int(percentage_dma))
df_pcnt= df_pcnt.append({'IP' : 'DMA', 'Total_Tests' : sub_total , 'Tests_Passed' : int(passed_dma) , 'Tests_Failed': int(failed_dma), 'Timeout' : int(timeout_dma), 'Percentage' : int(percentage_dma)},
        ignore_index = True)
passed_gbe=len(df_f[df_f['Status'].str.contains('Passed') & df_f['IP'].str.contains('GBE') ])
failed_gbe=len(df_f[df_f['Status'].str.contains('Failed') & df_f['IP'].str.contains('GBE') ])
timeout_gbe=len(df_f[df_f['Status'].str.contains('timeout') & df_f['IP'].str.contains('GBE')])

grand_total_passed=passed_gbe+grand_total_passed
#print("GBE Total Passed",passed_gbe)
grand_total_failed=failed_gbe+grand_total_failed
#print("GBE Total Failed",failed_gbe)
grand_total_timeout=timeout_gbe+grand_total_timeout
#print("GBE Total Timeout",timeout_gbe)
sub_total=passed_gbe+failed_gbe+timeout_gbe
percentage_gbe=(passed_gbe/sub_total)*100

#print("GBE Pass Percentage",int(percentage_gbe))
df_pcnt= df_pcnt.append({'IP' : 'GBE', 'Total_Tests' : sub_total , 'Tests_Passed' : int(passed_gbe) , 'Tests_Failed': int(failed_gbe), 'Timeout' : int(timeout_gbe), 'Percentage' : int(percentage_gbe)},
        ignore_index = True)
passed_fcb=len(df_f[df_f['Status'].str.contains('Passed') & df_f['IP'].str.contains('FCB') ])
failed_fcb=len(df_f[df_f['Status'].str.contains('Failed') & df_f['IP'].str.contains('FCB') ])
timeout_fcb=len(df_f[df_f['Status'].str.contains('timeout') & df_f['IP'].str.contains('FCB')])

grand_total_passed=passed_fcb+grand_total_passed
#print("FCB Total Passed",passed_fcb)
grand_total_failed=failed_fcb+grand_total_failed
#print("FCB Total Failed",failed_fcb)
grand_total_timeout=timeout_fcb+grand_total_timeout
#print("FCB Total Timeout",timeout_fcb)
sub_total=passed_fcb+failed_fcb+timeout_fcb
percentage_fcb=(passed_fcb/sub_total)*100

#print("FCB Pass Percentage",int(percentage_fcb))
df_pcnt= df_pcnt.append({'IP' : 'FCB', 'Total_Tests' : sub_total , 'Tests_Passed' : int(passed_fcb) , 'Tests_Failed': int(failed_fcb), 'Timeout' : int(timeout_fcb), 'Percentage' : int(percentage_fcb)},
        ignore_index = True)
passed_pcb=len(df_f[df_f['Status'].str.contains('Passed') & df_f['IP'].str.contains('PCB') ])
failed_pcb=len(df_f[df_f['Status'].str.contains('Failed') & df_f['IP'].str.contains('PCB') ])
timeout_pcb=len(df_f[df_f['Status'].str.contains('timeout') & df_f['IP'].str.contains('PCB')])

grand_total_passed=passed_pcb+grand_total_passed
#print("PCB Total Passed",passed_pcb)
grand_total_failed=failed_pcb+grand_total_failed
#print("PCB Total Failed",failed_pcb)
grand_total_timeout=timeout_pcb+grand_total_timeout
#print("PCB Total Timeout",timeout_pcb)
sub_total=passed_pcb+failed_pcb+timeout_pcb
percentage_pcb=(passed_pcb/sub_total)*100

#print("PCB Pass Percentage",int(percentage_pcb))
df_pcnt= df_pcnt.append({'IP' : 'PCB', 'Total_Tests' : sub_total , 'Tests_Passed' : int(passed_pcb) , 'Tests_Failed': int(failed_pcb), 'Timeout' : int(timeout_pcb), 'Percentage' : int(percentage_pcb)},
        ignore_index = True)
passed_gpt=len(df_f[df_f['Status'].str.contains('Passed') & df_f['IP'].str.contains('GPT') ])
failed_gpt=len(df_f[df_f['Status'].str.contains('Failed') & df_f['IP'].str.contains('GPT') ])
timeout_gpt=len(df_f[df_f['Status'].str.contains('timeout') & df_f['IP'].str.contains('GPT')])

grand_total_passed=passed_gpt+grand_total_passed
#print("GPT Total Passed",passed_gpt)
grand_total_failed=failed_gpt+grand_total_failed
#print("GPT Total Failed",failed_gpt)
grand_total_timeout=timeout_gpt+grand_total_timeout
#print("GPT Total Timeout",timeout_gpt)
sub_total=passed_gpt+failed_gpt+timeout_gpt
percentage_gpt=(passed_gpt/sub_total)*100

#print("GPT Pass Percentage",int(percentage_gpt))
df_pcnt= df_pcnt.append({'IP' : 'GPT', 'Total_Tests' : sub_total , 'Tests_Passed' : int(passed_gpt) , 'Tests_Failed': int(failed_gpt), 'Timeout' : int(timeout_gpt), 'Percentage' : int(percentage_gpt)},
        ignore_index = True)
passed_gpio=len(df_f[df_f['Status'].str.contains('Passed') & df_f['IP'].str.contains('GPIO') ])
failed_gpio=len(df_f[df_f['Status'].str.contains('Failed') & df_f['IP'].str.contains('GPIO') ])
timeout_gpio=len(df_f[df_f['Status'].str.contains('timeout') & df_f['IP'].str.contains('GPIO')])

grand_total_passed=passed_gpio+grand_total_passed
#print("GPIO Total Passed",passed_gpio)
grand_total_failed=failed_gpio+grand_total_failed
#print("GPIO Total Failed",failed_gpio)
grand_total_timeout=timeout_gpio+grand_total_timeout
#print("GPIO Total Timeout",timeout_gpio)
sub_total=passed_gpio+failed_gpio+timeout_gpio
percentage_gpio=(passed_gpio/sub_total)*100

#print("GPIO Pass Percentage",int(percentage_gpio))
df_pcnt= df_pcnt.append({'IP' : 'GPIO', 'Total_Tests' : sub_total , 'Tests_Passed' : int(passed_gpio) , 'Tests_Failed': int(failed_gpio), 'Timeout' : int(timeout_gpio), 'Percentage' : int(percentage_gpio)},
        ignore_index = True)
passed_wdt=len(df_f[df_f['Status'].str.contains('Passed') & df_f['IP'].str.contains('WDT') ])
failed_wdt=len(df_f[df_f['Status'].str.contains('Failed') & df_f['IP'].str.contains('WDT') ])
timeout_wdt=len(df_f[df_f['Status'].str.contains('timeout') & df_f['IP'].str.contains('WDT')])

grand_total_passed=passed_wdt+grand_total_passed
#print("WDT Total Passed",passed_wdt)
grand_total_failed=failed_wdt+grand_total_failed
#print("WDT Total Failed",failed_wdt)
grand_total_timeout=timeout_wdt+grand_total_timeout
#print("WDT Total Timeout",timeout_wdt)
sub_total=passed_wdt+failed_wdt+timeout_wdt
percentage_wdt=(passed_wdt/sub_total)*100

#print("WDT Pass Percentage",int(percentage_wdt))
df_pcnt= df_pcnt.append({'IP' : 'WDT', 'Total_Tests' : sub_total , 'Tests_Passed' : int(passed_wdt) , 'Tests_Failed': int(failed_wdt), 'Timeout' : int(timeout_wdt), 'Percentage' : int(percentage_wdt)},
        ignore_index = True)
passed_scu=len(df_f[df_f['Status'].str.contains('Passed') & df_f['IP'].str.contains('SCU') ])
failed_scu=len(df_f[df_f['Status'].str.contains('Failed') & df_f['IP'].str.contains('SCU') ])
timeout_scu=len(df_f[df_f['Status'].str.contains('timeout') & df_f['IP'].str.contains('SCU')])

grand_total_passed=passed_scu+grand_total_passed
#print("SCU Total Passed",passed_scu)
grand_total_failed=failed_scu+grand_total_failed
#print("SCU Total Failed",failed_scu)
grand_total_timeout=timeout_scu+grand_total_timeout
#print("SCU Total Timeout",timeout_scu)
sub_total=passed_scu+failed_scu+timeout_scu
percentage_scu=(passed_scu/sub_total)*100

#print("SCU Pass Percentage",int(percentage_scu))
df_pcnt= df_pcnt.append({'IP' : 'SCU', 'Total_Tests' : sub_total , 'Tests_Passed' : int(passed_scu) , 'Tests_Failed': int(failed_scu), 'Timeout' : int(timeout_scu), 'Percentage' : int(percentage_scu)},
        ignore_index = True)
passed_sram=len(df_f[df_f['Status'].str.contains('Passed') & df_f['IP'].str.contains('SRAM') ])
failed_sram=len(df_f[df_f['Status'].str.contains('Failed') & df_f['IP'].str.contains('SRAM') ])
timeout_sram=len(df_f[df_f['Status'].str.contains('timeout') & df_f['IP'].str.contains('SRAM')])

grand_total_passed=passed_sram+grand_total_passed
#print("SRAM Total Passed",passed_sram)
grand_total_failed=failed_sram+grand_total_failed
#print("SRAM Total Failed",failed_sram)
grand_total_timeout=timeout_sram+grand_total_timeout
#print("SRAM Total Timeout",timeout_sram)
sub_total=passed_sram+failed_sram+timeout_sram
percentage_sram=(passed_sram/sub_total)*100

#print("SRAM Pass Percentage",int(percentage_sram))
df_pcnt= df_pcnt.append({'IP' : 'SRAM', 'Total_Tests' : sub_total , 'Tests_Passed' : int(passed_sram) , 'Tests_Failed': int(failed_sram), 'Timeout' : int(timeout_sram), 'Percentage' : int(percentage_sram)},
        ignore_index = True)
# print(df_pcnt)


passed_pufcc=len(df_f[df_f['Status'].str.contains('Passed') & df_f['IP'].str.contains('PUFCC') ])
failed_pufcc=len(df_f[df_f['Status'].str.contains('Failed') & df_f['IP'].str.contains('PUFCC') ])
timeout_pufcc=len(df_f[df_f['Status'].str.contains('timeout') & df_f['IP'].str.contains('PUFCC')])

grand_total_passed=passed_pufcc+grand_total_passed
#print("SRAM Total Passed",passed_sram)
grand_total_failed=failed_pufcc+grand_total_failed
#print("SRAM Total Failed",failed_sram)
grand_total_timeout=timeout_pufcc+grand_total_timeout
#print("SRAM Total Timeout",timeout_sram)
sub_total=passed_pufcc+failed_pufcc+timeout_pufcc
percentage_pufcc=(passed_pufcc/sub_total)*100

#print("SRAM Pass Percentage",int(percentage_sram))
df_pcnt= df_pcnt.append({'IP' : 'PUFCC', 'Total_Tests' : sub_total , 'Tests_Passed' : int(passed_pufcc) , 'Tests_Failed': int(failed_pufcc), 'Timeout' : int(timeout_pufcc), 'Percentage' : int(percentage_pufcc)},
        ignore_index = True)
# print(df_pcnt)

### Temporary Insertions ###
passed_acpu=len(df_f[df_f['Status'].str.contains('Passed') & df_f['IP'].str.contains('REAL_ACPU') ])
failed_acpu=len(df_f[df_f['Status'].str.contains('Failed') & df_f['IP'].str.contains('REAL_ACPU') ])
timeout_acpu=len(df_f[df_f['Status'].str.contains('timeout') & df_f['IP'].str.contains('REAL_ACPU')])

grand_total_passed=passed_acpu+grand_total_passed

grand_total_failed=failed_acpu+grand_total_failed

grand_total_timeout=timeout_acpu+grand_total_timeout

sub_total=passed_acpu+failed_acpu+timeout_acpu
percentage_acpu=(passed_acpu/sub_total)*100


df_pcnt= df_pcnt.append({'IP' : 'REAL_ACPU', 'Total_Tests' : sub_total , 'Tests_Passed' : int(passed_acpu) , 'Tests_Failed': int(failed_acpu), 'Timeout' : int(timeout_acpu), 'Percentage' : int(percentage_acpu)},
        ignore_index = True)
# print(df_pcnt)
passed_bcpu=len(df_f[df_f['Status'].str.contains('Passed') & df_f['IP'].str.contains('REAL_BCPU') ])
failed_bcpu=len(df_f[df_f['Status'].str.contains('Failed') & df_f['IP'].str.contains('REAL_BCPU') ])
timeout_bcpu=len(df_f[df_f['Status'].str.contains('timeout') & df_f['IP'].str.contains('REAL_BCPU')])

grand_total_passed=passed_bcpu+grand_total_passed

grand_total_failed=failed_bcpu+grand_total_failed

grand_total_timeout=timeout_bcpu+grand_total_timeout

sub_total=passed_bcpu+failed_bcpu+timeout_bcpu
percentage_bcpu=(passed_bcpu/sub_total)*100


df_pcnt= df_pcnt.append({'IP' : 'REAL_BCPU', 'Total_Tests' : sub_total , 'Tests_Passed' : int(passed_bcpu) , 'Tests_Failed': int(failed_bcpu), 'Timeout' : int(timeout_bcpu), 'Percentage' : int(percentage_bcpu)},
        ignore_index = True)


# passed_abcpu=len(df_f[df_f['Status'].str.contains('Passed') & df_f['IP'].str.contains('REAL_ABCPU') ])
# failed_abcpu=len(df_f[df_f['Status'].str.contains('Failed') & df_f['IP'].str.contains('REAL_ABCPU') ])
# timeout_abcpu=len(df_f[df_f['Status'].str.contains('timeout') & df_f['IP'].str.contains('REAL_ABCPU')])

# grand_total_passed=passed_abcpu+grand_total_passed

# grand_total_failed=failed_abcpu+grand_total_failed

# grand_total_timeout=timeout_abcpu+grand_total_timeout

# sub_total=passed_abcpu+failed_abcpu+timeout_abcpu
# percentage_abcpu=(passed_abcpu/sub_total)*100


# df_pcnt= df_pcnt.append({'IP' : 'REAL_ABCPU', 'Total_Tests' : sub_total , 'Tests_Passed' : int(passed_abcpu) , 'Tests_Failed': int(failed_abcpu), 'Timeout' : int(timeout_abcpu), 'Percentage' : int(percentage_abcpu)},
#         ignore_index = True)








passed_ddr3=len(df_f[df_f['Status'].str.contains('Passed') & df_f['IP'].str.contains('^DDR3') ])
failed_ddr3=len(df_f[df_f['Status'].str.contains('Failed') & df_f['IP'].str.contains('^DDR3') ])
timeout_ddr3=len(df_f[df_f['Status'].str.contains('timeout') & df_f['IP'].str.contains('^DDR3')])

grand_total_passed=passed_ddr3+grand_total_passed
#print("SRAM Total Passed",passed_sram)
grand_total_failed=failed_ddr3+grand_total_failed
#print("SRAM Total Failed",failed_sram)
grand_total_timeout=timeout_ddr3+grand_total_timeout
#print("SRAM Total Timeout",timeout_sram)
sub_total=passed_ddr3+failed_ddr3+timeout_ddr3
percentage_ddr3=(passed_ddr3/sub_total)*100

#print("SRAM Pass Percentage",int(percentage_sram))
df_pcnt= df_pcnt.append({'IP' : 'DDR3', 'Total_Tests' : sub_total , 'Tests_Passed' : int(passed_ddr3) , 'Tests_Failed': int(failed_ddr3), 'Timeout' : int(timeout_ddr3), 'Percentage' : int(percentage_ddr3)},
        ignore_index = True)
# print(df_pcnt)


# passed_ddr4=len(df_f[df_f['Status'].str.contains('Passed') & df_f['IP'].str.contains('DDR4') ])
# failed_ddr4=len(df_f[df_f['Status'].str.contains('Failed') & df_f['IP'].str.contains('DDR4') ])
# timeout_ddr4=len(df_f[df_f['Status'].str.contains('timeout') & df_f['IP'].str.contains('DDR4')])
# grand_total_passed=passed_ddr4+grand_total_passed
# grand_total_failed=failed_ddr4+grand_total_failed
# grand_total_timeout=timeout_ddr4+grand_total_timeout
# sub_total=passed_ddr4+failed_ddr4+timeout_ddr4
# percentage_ddr4=(passed_ddr4/sub_total)*100
# df_pcnt= df_pcnt.append({'IP' : 'DDR4', 'Total_Tests' : sub_total , 'Tests_Passed' : int(passed_ddr4) , 'Tests_Failed': int(failed_ddr4), 'Timeout' : int(timeout_ddr4), 'Percentage' : int(percentage_ddr4)},
#         ignore_index = True)
# # print(df_pcnt)


passed_lpddr3=len(df_f[df_f['Status'].str.contains('Passed') & df_f['IP'].str.contains('LPDDR3') ])
failed_lpddr3=len(df_f[df_f['Status'].str.contains('Failed') & df_f['IP'].str.contains('LPDDR3') ])
timeout_lpddr3=len(df_f[df_f['Status'].str.contains('timeout') & df_f['IP'].str.contains('LPDDR3')])
grand_total_passed=passed_lpddr3+grand_total_passed
grand_total_failed=failed_lpddr3+grand_total_failed
grand_total_timeout=timeout_lpddr3+grand_total_timeout
sub_total=passed_lpddr3+failed_lpddr3+timeout_lpddr3
percentage_lpddr3=(passed_lpddr3/sub_total)*100
df_pcnt= df_pcnt.append({'IP' : 'LPDDR3', 'Total_Tests' : sub_total , 'Tests_Passed' : int(passed_lpddr3) , 'Tests_Failed': int(failed_lpddr3), 'Timeout' : int(timeout_lpddr3), 'Percentage' : int(percentage_lpddr3)},
        ignore_index = True)
# print(df_pcnt)

# passed_lpddr4=len(df_f[df_f['Status'].str.contains('Passed') & df_f['IP'].str.contains('LPDDR4') ])
# failed_lpddr4=len(df_f[df_f['Status'].str.contains('Failed') & df_f['IP'].str.contains('LPDDR4') ])
# timeout_lpddr4=len(df_f[df_f['Status'].str.contains('timeout') & df_f['IP'].str.contains('LPDDR4')])
# grand_total_passed=passed_lpddr4+grand_total_passed
# grand_total_failed=failed_lpddr4+grand_total_failed
# grand_total_timeout=timeout_lpddr4+grand_total_timeout
# sub_total=passed_lpddr4+failed_lpddr4+timeout_lpddr4
# percentage_lpddr4=(passed_lpddr4/sub_total)*100
# df_pcnt= df_pcnt.append({'IP' : 'LPDDR4', 'Total_Tests' : sub_total , 'Tests_Passed' : int(passed_lpddr4) , 'Tests_Failed': int(failed_lpddr4), 'Timeout' : int(timeout_lpddr4), 'Percentage' : int(percentage_lpddr4)},
#         ignore_index = True)
# # print(df_pcnt)






grand_total=grand_total_passed+grand_total_failed+grand_total_timeout
total_percentage=int((grand_total_passed/grand_total)*100)
#print("Overall Percentage",total_percentage)
#print("Total Tests Executed",grand_total)
df_pcnt= df_pcnt.append({'IP' : 'Aggregate', 'Total_Tests' : grand_total , 'Tests_Passed' : int(grand_total_passed) , 'Tests_Failed': int(grand_total_failed), 'Timeout' : int(grand_total_timeout), 'Percentage' : int(total_percentage)},
        ignore_index = True)

print(df_pcnt)
image_path = 'assets/huge.png'


########
#app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
app = Dash(__name__,external_stylesheets=[dbc.themes.CYBORG])
theme = {
    'dark': True,
    'detail': '#007439',
    'primary': '#00EA64',
    'secondary': '#6E6E6E',
}
server = app.server
fig = px.pie(df_grp_dash, values='Numbers', names='Category',color = "Category",hole=.2,color_discrete_map={'Tests Passed':'#66CDAA',
                                 'Tests Under Regression':'#FFA500',                                                                           
                                 'Tests Failed':'#CD5C5C'})
fig.update_layout(title={'text': '<b>Pie Chart SoC</b>','y':0.95,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'},
font={'size': 15},
title_font_color='black',
legend=dict(
    yanchor="top",
    y=1,
    xanchor="left",
    x=1,
))

fig_sram = px.pie(sram_df_grp_dash, values='Numbers', names='Category',color = "Category",hole=.2,color_discrete_map={'Tests Passed':'#66CDAA',
                                 'Tests Under Development':'#00BFFF',                                                                           
                                 'Tests Failed':'#CD5C5C'})
fig_sram.update_layout(title={'text': '<b>Pie Chart SRAM  (Unit Level)</b>','y':0.95,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'},
font={'size': 15},
title_font_color='black',
legend=dict(
    yanchor="top",
    y=0.99,
    xanchor="left",
    x=0.00,
))

fig_fcb = px.pie(fcb_df_grp_dash, values='Numbers', names='Category',color = "Category",hole=.2,color_discrete_map={'Tests Passed':'#66CDAA',
                                 'Tests Under Development':'#00BFFF',                                                                           
                                 'Tests Failed':'#CD5C5C'})
fig_fcb.update_layout(title={'text': '<b>Pie Chart FCB  (Unit Level)</b>','y':1,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'},
font={'size': 15},
title_font_color='black',
legend=dict(
    yanchor="top",
    y=0.99,
    xanchor="left",
    x=0.00,
))

arr =[158,158,158,158,158,158,250,250,250,250,420,439,525]
aarr= [21,35,39,56,65,96,139,167,171,195,360,379,487]
arr_f= [0,3,3,0,4,15,39,37,30,50,50,37,29]
arr_x=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17]
f1 = go.Figure(
    data = [
        go.Scatter(x=arr_x,y=arr, name="Tests Planned",line=dict(color="#00BFFF")),
        go.Scatter(x=arr_x,y=aarr, name="Tests Passed",line=dict(color="#66CDAA")),
        go.Scatter(x=arr_x,y=arr_f, name="Tests Failed",line=dict(color="#CD5C5C")),
    ],
    layout = {"xaxis": {"title": "Weeks"}, "yaxis": {"title": "No. of Tests"}, "title": "Weekly Statistics"}
)
f1.update_layout(title={'text': '<b>Weekly Statistics SoC</b>','y':0.9,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'},
font={'size': 15},
title_font_color='black',
# legend=dict(
#     yanchor="top",
#     y=0.99,
#     xanchor="left",
#     x=0.00,
# ))
# width=1300,
# height=600
)
# f1.update_layout(width=int(width))

app.layout = html.Div(style = {
#   'backgroundColor': '#FFFFFF',
  'fontSize' : '100'
}, children = [
#     html.H1(
#     children = 'RapidSilicon',
#     style = {
#       'textAlign': 'center',
#       'color': 'Crimson',
#       'fontWeight': 'bold',
#       'font-size':'xx-large',
#       'text-decoration-line': 'underline',
#     }
    
#   ),
 html.Div([
         html.Img(src='assets/RS-Logo-For-White-Background.jpg',
            style={
                'height': '20%',
                'width': '25%'
            })
], style={'textAlign': 'center'}),
    html.Div(children = 'Gemini SoC Tests Statistics', style = {
    'textAlign': 'center',
    # 'color': '#7FDBFF',
    'color': 'blue',
    'fontWeight': 'bold',
    'font-size':'x-large',
  }),

dcc.Markdown('''
    [](/)
'''),
 dcc.Markdown('''
    [](/)
'''),
 dcc.Markdown('''
    [](/)
'''),
 dcc.Markdown('''
    [](/)
'''),
 dcc.Markdown('''
    [](/)
'''),
 dcc.Markdown('''
    [](/)
'''),
 dcc.Markdown('''
    [](/)
'''),
 dcc.Markdown('''
    [](/)
'''),
#   html.Div(children = df_time_lg["Regression_Run_Time"], style = {
#     'textAlign': 'left',
#     'color': '#7FDBFF',
#     'fontWeight': 'bold'
#   }),
#  dcc.Graph(
#     id = 'gemini-graph-1',
#     figure = fig
#   ),
dbc.Container([
  html.Div(children = "Regression Date:   "+df_time_lg["Regression_Run_Time"], style = {
     'textAlign': 'left',
     'color': 'Black',
     'fontWeight': 'bold'
   }),
 dcc.Markdown('''
    [](/)
'''),
 dcc.Markdown('''
    [](/)
'''),
 dcc.Markdown('''
    [](/)
'''),
 dcc.Markdown('''
    [](/)
'''),
 dcc.Graph(
    id = 'gemini-graph-1',
    figure = fig
  ),

html.Div(children = 'General Statistics', style = {
    'textAlign': 'center',
    # 'color': '#7FDBFF',
    'color': 'black',
    'fontWeight': 'bold',
    'font-size':'large',
  }),
 dcc.Markdown('''
    [](/)
'''),
 dcc.Markdown('''
    [](/)
'''),
 dcc.Markdown('''
    [](/)
'''),
 dcc.Markdown('''
    [](/)
'''),
dash_table.DataTable(    style_data={
        'whiteSpace': 'normal',
        'height': 'auto',
        'textAlign': 'center',
        'lineHeight': '10px',
    },
    data=df_table.to_dict('records'),
    export_format="csv",
    columns=[{"name": i, "id": i} for i in df_table.columns],
        css=[{"selector": "input", "rule": "color:gray"}],
            # data=df.to_dict("records"),
            style_cell={"color": "gray"},
            # editable=True,
            style_data_conditional=[
                {"if": {"row_index": 0}, "backgroundColor": "#00BFFF"},
                {"if": {"row_index": 1}, "backgroundColor": "#66CDAA"},
                {"if": {"row_index": 2}, "backgroundColor": "#CD5C5C"},
                {"if": {"row_index": 3}, "backgroundColor": "#FFA500"},
                {
                    "if": {"state": "active"},
                    "backgroundColor": "inherit !important",
                    "border": "1px solid black",
                    ## "color": "gray",
                },
                {
                    "if": {"state": "selected"},
                    "backgroundColor": "inherit !important",
                    # "border": "1px solid blue",
                },
        {
            'if': {
                'filter_query': '{Numbers} > 0',
                'row_index': 2,
            },
            'backgroundColor': '#CD5C5C',
            'color': 'black'
         },
            ],
        style_cell_conditional=[
        {'if': {'column_id': 'Category'},
         'width': '10%',
         'textAlign': 'center',
         'fontWeight': 'bold',
         'color': 'BLACK'},
        {'if': {'column_id': 'Numbers'},
         'width': '10%',
         'textAlign': 'center',
         'fontWeight': 'bold',
         'color': 'BLACK'},
    ]),
 dcc.Markdown('''
    [](/)
'''),
 dcc.Markdown('''
    [](/)
'''),
 dcc.Markdown('''
    [](/)
'''),
 dcc.Markdown('''
    [](/)
'''),
 dcc.Markdown('''
    [](/)
'''),
 dcc.Markdown('''
    [](/)
'''),
 dcc.Markdown('''
    [](/)
'''),
 dcc.Markdown('''
    [](/)
'''),
# html.Div(children = 'Weekly Scatter Plot', style = {
#     'textAlign': 'left',
#     'color': 'black',
#     'fontWeight': 'bold'
#   }),
    dcc.Graph(
    id = 'gemini-graph-2',
    figure = f1
  ),
 dcc.Markdown('''
    [](/)
'''),
 dcc.Markdown('''
    [](/)
'''),
 dcc.Markdown('''
    [](/)
'''),
 dcc.Markdown('''
    [](/)
'''),
html.Div(children = 'IP-wise Summary', style = {
    'textAlign': 'center',
    # 'color': '#7FDBFF',
    'color': 'black',
    'fontWeight': 'bold',
    'font-size':'large',
  }),
 dcc.Markdown('''
    [](/)
'''),
 dcc.Markdown('''
    [](/)
'''),
 dcc.Markdown('''
    [](/)
'''),
 dcc.Markdown('''
    [](/)
'''),
dash_table.DataTable(    style_data={
        'whiteSpace': 'normal',
        'height': 'auto',
        'textAlign': 'center',
        'lineHeight': '10px',
    },
    data=df_pcnt.to_dict('records'),
    export_format="csv",
    columns=[{"name": i, "id": i} for i in df_pcnt.columns],
    style_as_list_view=True,
    style_header={
        'backgroundColor': 'white',
        'fontWeight': 'bold'
    },
        css=[{"selector": "input", "rule": "color:gray"}],
            # data=df.to_dict("records"),
            style_cell={"color": "black"},
            # editable=True,
            style_data_conditional=[
#             {"if": {"row_index": 0}, "backgroundColor": "#F08080"},
                {
            'if': {
                'filter_query': '{IP} contains "Aggregate"'
            },
            'backgroundColor': '#0074D9',
            'color': 'white'
        },
#                        {
#             'if': {
#                 'filter_query': '{IP}'
#             },
#             'backgroundColor': '#F08080',
#             'color': 'white'
#         },
                {
                    "if": {"state": "active"},
                    "backgroundColor": "inherit !important",
                    "border": "1px solid black",
                    ## "color": "gray",
                },
                {
                    "if": {"state": "selected"},
                    "backgroundColor": "inherit !important",
                    # "border": "1px solid blue",
                },
                {
                 'if': {
                'filter_query': '{Percentage} > 89',
                'column_id': 'Percentage'
            },
            'backgroundColor': '#66CDAA',
            'color': 'black'
         },
               
          {
            'if': {
                'filter_query': '{Percentage} > 79 && {Percentage} < 90',
                 'column_id': 'Percentage'
            },
            'backgroundColor': '#ffff66',
            'color': 'black'
         },         
          
          {
              'if': {
                'filter_query': '{Percentage} < 80',
                'column_id': 'Percentage'
            },
            'backgroundColor': '#CD5C5C',
            'color': 'black'
         }, 
                     ],
        style_cell_conditional=[
        {'if': {'column_id': 'IP'},
         'width': '10%',
         'textAlign': 'center',
         'fontWeight': 'bold',
         'color': 'BLACK',
        'backgroundColor': '#8A2BE2',
        },
        {'if': {'column_id': 'Total_Tests'},
         'width': '10%',
         'textAlign': 'center',
         'fontWeight': 'bold',
         'color': 'BLACK',
         'backgroundColor': '#87CEFA',        
        },
        {'if': {'column_id': 'Tests_Passed'},
         'width': '10%',
         'textAlign': 'center',
         'fontWeight': 'bold',
         'color': 'BLACK',
        'backgroundColor': '#66CDAA',
        },
        {'if': {'column_id': 'Tests_Failed'},
         'width': '10%',
         'textAlign': 'center',
         'fontWeight': 'bold',
         'color': 'BLACK',
        'backgroundColor': '#CD5C5C',
        },
       {'if': {'column_id': 'Timeout'},
         'width': '10%',
         'textAlign': 'center',
         'fontWeight': 'bold',
         'color': 'BLACK',
         'backgroundColor': '#FFFF00',
       },
      {'if': {'column_id': 'Percentage'},
         'width': '10%',
         'textAlign': 'center',
         'fontWeight': 'bold',
         'color': 'BLACK',
       'backgroundColor': '#00FF00 ',
      },
      
    ]),
 dcc.Markdown('''
    [](/)
'''),
 dcc.Markdown('''
    [](/)
'''),
 dcc.Markdown('''
    [](/)
'''),
 dcc.Markdown('''
    [](/)
'''),
 dcc.Markdown('''
    [](/)
'''),
 dcc.Markdown('''
    [](/)
'''),
 dcc.Markdown('''
    [](/)
'''),
 dcc.Markdown('''
    [](/)
'''),

html.Div(children = 'IP-wise Statistics', style = {
    'textAlign': 'center',
    # 'color': '#7FDBFF',
    'color': 'black',
    'fontWeight': 'bold',
    'font-size':'large',
  }),
 dcc.Markdown('''
    [](/)
'''),
 dcc.Markdown('''
    [](/)
'''),
 dcc.Markdown('''
    [](/)
'''),
 dcc.Markdown('''
    [](/)
'''),
    # dcc.Markdown('# DataTable Tips and Tricks', style={'textAlign':'center'}),

    dbc.Label("Show number of rows:"),
     dcc.Markdown('''
    [](/)
'''),
 dcc.Markdown('''
    [](/)
'''),
 dcc.Markdown('''
    [](/)
'''),
 dcc.Markdown('''
    [](/)
'''),
    row_drop := dcc.Dropdown(value=10, clearable=False, style={'width':'35%'},
                             options=[10, 25, 50, 100]),
        dbc.Row([
        dbc.Col([
            IP_drop := dcc.Dropdown([x for x in sorted(df_f.IP.unique())])
        ], width=3),

    ], justify="between", className='mt-3 mb-4'),

    my_table := dash_table.DataTable(
        columns=[
            {'name': 'Sr#', 'id': 'Sr#', 'type': 'text'},
            {'name': 'IP', 'id': 'IP', 'type': 'text'},
            {'name': 'Test_Name', 'id': 'Test_Name', 'type': 'text'},
            {'name': 'Status', 'id': 'Status', 'type': 'text'},
            {'name': 'Remarks', 'id': 'Remarks', 'type': 'text'}
        ],
        style_table={'overflowX': 'auto'},
        data=df_f.to_dict('records'),
        export_format="csv",
        filter_action='native',
        page_size=10,
           style_data={
        'whiteSpace': 'normal',
        'height': 'auto',
        'textAlign': 'center',
        # 'lineHeight': '10px'
    },
            # editable=True,
            style_data_conditional=[
                {"if": {"row_index": "odd"}, "backgroundColor": "#66CDAA"},
                {"if": {"row_index": "even"}, "backgroundColor": "#66CDAA"},
                {
                    "if": {"state": "active"},
                    "backgroundColor": "inherit !important",
                    "border": "1px solid black",
                    # "color": "gray",
                },
                # {
                #     "if": {"state": "selected"},
                #     "backgroundColor": "black",
                #     # "border": "1px solid blue",
                # },
                   {"if": {"state": "selected"},
                         "backgroundColor": "inherit !important",
                          "border": "inherit !important",},
            {
            'if': {
                'filter_query': '{Status} contains "Failed"',
                'column_id': 'Status'
            },
            'backgroundColor': '#CD5C5C',
            'color': 'black'
         },
            {
            'if': {
                'filter_query': '{Status} contains "timeout"',
                'column_id': 'Status'
            },
            'backgroundColor': '#CD5C5C',
            'color': 'black'
         },

            ],
        style_cell_conditional=[
        {'if': {'column_id': 'Sr#'},
         'width': '10%',
         'textAlign': 'center',
            'color': 'BLACK',
            'fontWeight': 'bold'},
        {'if': {'column_id': 'IP'},
         'width': '10%',
         'textAlign': 'center',
            'color': 'BLACK',
            'fontWeight': 'bold'},
        {'if': {'column_id': 'Test_Name'},
         'width': '10%',
         'textAlign': 'center',
         'color': 'BLACK',
         'fontWeight': 'bold'},
                {'if': {'column_id': 'Status'},
         'width': '10%',
         'textAlign': 'center',
         'color': 'BLACK',
         'fontWeight': 'bold'},
                 {'if': {'column_id': 'Remarks'},
         'width': '50%',
         'textAlign': 'center',
         'color': 'BLACK',
         'fontWeight': 'bold'
         },
         
    ]),
html.Div(children = 'Combined Coverage Report:', style = {
    'textAlign': 'left',
    'color': 'BLACK',
    'fontWeight': 'bold'
  }),
 dcc.Markdown('''
    [](/)
'''),
 dcc.Markdown('''
    [](/)
'''),
 dcc.Markdown('''
    [](/)
'''),
 dcc.Markdown('''
    [](/)
'''),

 html.Div(
    
    children=[
        html.Iframe(
            src="assets/soc/dashboard.html",
            style={"height": "1067px", "width": "100%"},
        )
    ]
    
),
 dcc.Markdown('''
    [](/)
'''),
 dcc.Markdown('''
    [](/)
'''),
 dcc.Markdown('''
    [](/)
'''),
 dcc.Markdown('''
    [](/)
'''),

    html.Div(children = 'SRAM  (Unit Level) Tests Statistics', style = {
    'textAlign': 'center',
    # 'color': '#7FDBFF',
    'color': 'blue',
    'fontWeight': 'bold',
    'font-size':'x-large',
  }),
 dcc.Markdown('''
    [](/)
'''),
 dcc.Markdown('''
    [](/)
'''),
 dcc.Markdown('''
    [](/)
'''),
 dcc.Markdown('''
    [](/)
'''),
 dcc.Markdown('''
    [](/)
'''),
 dcc.Markdown('''
    [](/)
'''),
 dcc.Markdown('''
    [](/)
'''),
 dcc.Markdown('''
    [](/)
'''),
 dcc.Graph(
    id = 'gemini-graph-sram',
    figure = fig_sram
  ),
html.Div(children = 'General Statistics SRAM  (Unit Level)', style = {
    'textAlign': 'center',
    # 'color': '#7FDBFF',
    'color': 'black',
    'fontWeight': 'bold',
    'font-size':'large',
  }),
 dcc.Markdown('''
    [](/)
'''),
 dcc.Markdown('''
    [](/)
'''),
 dcc.Markdown('''
    [](/)
'''),
 dcc.Markdown('''
    [](/)
'''),
dash_table.DataTable(    style_data={
        'whiteSpace': 'normal',
        'height': 'auto',
        'textAlign': 'center',
        'lineHeight': '10px'
    },
    data=sram_df_table.to_dict('records'),
    export_format="csv",
    columns=[{"name": i, "id": i} for i in sram_df_table.columns],
        css=[{"selector": "input", "rule": "color:gray"}],
            # data=df.to_dict("records"),
            style_cell={"color": "gray"},
            # editable=True,
            style_data_conditional=[
                {"if": {"row_index": 0}, "backgroundColor": "#00BFFF"},
                {"if": {"row_index": 1}, "backgroundColor": "#66CDAA"},
                {"if": {"row_index": 2}, "backgroundColor": "#CD5C5C"},
                {
                    "if": {"state": "active"},
                    "backgroundColor": "inherit !important",
                    "border": "1px solid black",
                    # "color": "gray",
                },
                {
                    "if": {"state": "selected"},
                    "backgroundColor": "inherit !important",
                    # "border": "1px solid blue",
                },
        {
            'if': {
                'filter_query': '{Numbers} > 0',
                'row_index': 2,
            },
            'backgroundColor': '#CD5C5C',
            'color': 'black'
         },
            ],
        style_cell_conditional=[
        {'if': {'column_id': 'Category'},
         'width': '10%',
         'textAlign': 'center',
         'fontWeight': 'bold',
         'color': 'BLACK'},
        {'if': {'column_id': 'Numbers'},
         'width': '10%',
         'textAlign': 'center',
         'fontWeight': 'bold',
         'color': 'BLACK'},
    ]),
 dcc.Markdown('''
    [](/)
'''),
 dcc.Markdown('''
    [](/)
'''),
 dcc.Markdown('''
    [](/)
'''),
 dcc.Markdown('''
    [](/)
'''),
html.Div(children = 'Test-wise Statistics', style = {
    'textAlign': 'center',
    # 'color': '#7FDBFF',
    'color': 'black',
    'fontWeight': 'bold',
    'font-size':'large',
  }),
 dcc.Markdown('''
    [](/)
'''),
 dcc.Markdown('''
    [](/)
'''),
 dcc.Markdown('''
    [](/)
'''),
 dcc.Markdown('''
    [](/)
'''),
dbc.Label("Show number of rows for sram tests:"),
    sram_row_drop := dcc.Dropdown(value=10, clearable=False, style={'width':'35%'},
                             options=[10, 25, 50, 100]),
        dbc.Row([
        dbc.Col([
            sram_test_name_drop := dcc.Dropdown([x for x in sorted(sram_df_f.Test_Name.unique())])
        ], width=3),

    ], 
    justify="between", className='mt-3 mb-4'),

    my_table_sram := dash_table.DataTable(
        columns=[
            {'name': 'Test_Name', 'id': 'Test_Name', 'type': 'text'},
            {'name': 'Status', 'id': 'Status', 'type': 'text'},
            {'name': 'Remarks', 'id': 'Remarks', 'type': 'text'}
        ],
        style_table={'overflowX': 'auto'},
        data=sram_df_f.to_dict('records'),
        export_format="csv",
        filter_action='native',
        page_size=10,
           style_data={
        'whiteSpace': 'normal',
        'height': 'auto',
        'textAlign': 'center',
        # 'lineHeight': '10px'
    },
            # editable=True,
            style_data_conditional=[
                {"if": {"row_index": "odd"}, "backgroundColor": "#66CDAA"},
                {"if": {"row_index": "even"}, "backgroundColor": "#66CDAA"},
                {
                    "if": {"state": "active"},
                    "backgroundColor": "inherit !important",
                    "border": "1px solid black",
                    # "color": "gray",
                },
                # {
                #     "if": {"state": "selected"},
                #     "backgroundColor": "black",
                #     # "border": "1px solid blue",
                # },
                   {"if": {"state": "selected"},
                         "backgroundColor": "inherit !important",
                          "border": "inherit !important",},
            {
            'if': {
                'filter_query': '{Status} contains "Failed"',
                'column_id': 'Status'
            },
            'backgroundColor': '#CD5C5C',
            'color': 'black'
         },
            {
            'if': {
                'filter_query': '{Status} contains "timeout"',
                'column_id': 'Status'
            },
            'backgroundColor': '#CD5C5C',
            'color': 'black'
         },
            ],
        style_cell_conditional=[
        {'if': {'column_id': 'Test_Name'},
         'width': '10%',
         'textAlign': 'center',
         'color': 'BLACK',
         'fontWeight': 'bold'},
                {'if': {'column_id': 'Status'},
         'width': '10%',
         'textAlign': 'center',
         'color': 'BLACK',
         'fontWeight': 'bold'},
                 {'if': {'column_id': 'Remarks'},
         'width': '50%',
         'textAlign': 'center',
         'color': 'BLACK',
         'fontWeight': 'bold'
         },
         
    ]),
html.Div(children = 'Coverage Report SRAM:', style = {
    'textAlign': 'left',
    'color': 'BLACK',
    'fontWeight': 'bold'
  }),
 dcc.Markdown('''
    [](/)
'''),
 dcc.Markdown('''
    [](/)
'''),
 dcc.Markdown('''
    [](/)
'''),
 dcc.Markdown('''
    [](/)
'''),
html.Div(children = html.Iframe(
            src="assets/sram/dashboard.html",
            style={"height": "1067px", "width": "100%"},
        )
  ),
 dcc.Markdown('''
    [](/)
'''),
 dcc.Markdown('''
    [](/)
'''),
 dcc.Markdown('''
    [](/)
'''),
 dcc.Markdown('''
    [](/)
'''),

    html.Div(children = 'FCB  (Unit Level) Tests Statistics', style = {
    'textAlign': 'center',
    # 'color': '#7FDBFF',
    'color': 'blue',
    'fontWeight': 'bold',
    'font-size':'x-large',
  }),
dcc.Markdown('''
    [](/)
'''),
 dcc.Markdown('''
    [](/)
'''),
 dcc.Markdown('''
    [](/)
'''),
 dcc.Markdown('''
    [](/)
'''),
 dcc.Graph(
    id = 'gemini-graph-fcb',
    figure = fig_fcb
  ),
html.Div(children = 'General Statistics FCB  (Unit Level)', style = {
    'textAlign': 'center',
    # 'color': '#7FDBFF',
    'color': 'black',
    'fontWeight': 'bold',
    'font-size':'large',
  }),
dash_table.DataTable(    style_data={
        'whiteSpace': 'normal',
        'height': 'auto',
        'textAlign': 'center',
        'lineHeight': '10px'
    },
    data=fcb_df_table.to_dict('records'),
    export_format="csv",
    columns=[{"name": i, "id": i} for i in fcb_df_table.columns],
        css=[{"selector": "input", "rule": "color:gray"}],
            # data=df.to_dict("records"),
            style_cell={"color": "gray"},
            # editable=True,
            style_data_conditional=[
                {"if": {"row_index": 0}, "backgroundColor": "#00BFFF"},
                {"if": {"row_index": 1}, "backgroundColor": "#66CDAA"},
                {"if": {"row_index": 2}, "backgroundColor": "#CD5C5C"},
                {
                    "if": {"state": "active"},
                    "backgroundColor": "inherit !important",
                    "border": "1px solid black",
                    # "color": "gray",
                },
                {
                    "if": {"state": "selected"},
                    "backgroundColor": "inherit !important",
                    # "border": "1px solid blue",
                },
        {
            'if': {
                'filter_query': '{Numbers} > 0',
                'row_index': 2,
            },
            'backgroundColor': '#CD5C5C',
            'color': 'black'
         },
            ],
        style_cell_conditional=[
        {'if': {'column_id': 'Category'},
         'width': '10%',
         'textAlign': 'center',
         'fontWeight': 'bold',
         'color': 'BLACK'},
        {'if': {'column_id': 'Numbers'},
         'width': '10%',
         'textAlign': 'center',
         'fontWeight': 'bold',
         'color': 'BLACK'},
    ]),
 dcc.Markdown('''
    [](/)
'''),
 dcc.Markdown('''
    [](/)
'''),
 dcc.Markdown('''
    [](/)
'''),
 dcc.Markdown('''
    [](/)
'''),
html.Div(children = 'Test-wise Statistics', style = {
    'textAlign': 'center',
    # 'color': '#7FDBFF',
    'color': 'black',
    'fontWeight': 'bold',
    'font-size':'large',
  }),
 dcc.Markdown('''
    [](/)
'''),
 dcc.Markdown('''
    [](/)
'''),
 dcc.Markdown('''
    [](/)
'''),
 dcc.Markdown('''
    [](/)
'''),
dbc.Label("Show number of rows for fcb tests:"),
    fcb_row_drop := dcc.Dropdown(value=10, clearable=False, style={'width':'35%'},
                             options=[10, 25, 50, 100]),
        dbc.Row([
        dbc.Col([
            fcb_test_name_drop := dcc.Dropdown([x for x in sorted(fcb_df_f.Test_Name.unique())])
        ], width=3),

    ], 
    justify="between", className='mt-3 mb-4'),

    my_table_fcb := dash_table.DataTable(
        columns=[
            {'name': 'Test_Name', 'id': 'Test_Name', 'type': 'text'},
            {'name': 'Status', 'id': 'Status', 'type': 'text'},
            {'name': 'Remarks', 'id': 'Remarks', 'type': 'text'}
        ],
        style_table={'overflowX': 'auto'},
        data=fcb_df_f.to_dict('records'),
        export_format="csv",
        filter_action='native',
        page_size=10,
           style_data={
        'whiteSpace': 'normal',
        'height': 'auto',
        'textAlign': 'center',
        # 'lineHeight': '10px'
    },
            # editable=True,
            style_data_conditional=[
                {"if": {"row_index": "odd"}, "backgroundColor": "#66CDAA"},
                {"if": {"row_index": "even"}, "backgroundColor": "#66CDAA"},
                {
                    "if": {"state": "active"},
                    "backgroundColor": "inherit !important",
                    "border": "1px solid black",
                    # "color": "gray",
                },
                # {
                #     "if": {"state": "selected"},
                #     "backgroundColor": "black",
                #     # "border": "1px solid blue",
                # },
                   {"if": {"state": "selected"},
                         "backgroundColor": "inherit !important",
                          "border": "inherit !important",},
            {
            'if': {
                'filter_query': '{Status} contains "Failed"',
                'column_id': 'Status'
            },
            'backgroundColor': '#CD5C5C',
            'color': 'black'
         },

            ],
        style_cell_conditional=[
        {'if': {'column_id': 'Test_Name'},
         'width': '10%',
         'textAlign': 'center',
         'color': 'BLACK',
         'fontWeight': 'bold'},
                {'if': {'column_id': 'Status'},
         'width': '10%',
         'textAlign': 'center',
         'color': 'BLACK',
         'fontWeight': 'bold'},
                 {'if': {'column_id': 'Remarks'},
         'width': '50%',
         'textAlign': 'center',
         'color': 'BLACK',
         'fontWeight': 'bold'
         },
         
    ]),
html.Div(children = 'Coverage Report FCB:', style = {
    'textAlign': 'left',
    'color': 'Black',
    'fontWeight': 'bold'
  }),
dcc.Markdown('''
    [](/)
'''),
 dcc.Markdown('''
    [](/)
'''),
 dcc.Markdown('''
    [](/)
'''),
 dcc.Markdown('''
    [](/)
'''),
html.Div(children = html.Iframe(
            src="assets/fcb/dashboard.html",
            style={"height": "1067px", "width": "100%"},
        )
  ),

])
])
@callback(
    Output(my_table, 'data'),
    Output(my_table, 'page_size'),
    Input(IP_drop, 'value'),
    Input(row_drop, 'value'),)
def update_dropdown_options(IP_v,row_v):
    dff = df_f.copy()
    if IP_v:
        dff = dff[dff.IP==IP_v]
    return dff.to_dict('records'), row_v
@callback(
    Output(my_table_sram, 'data'),
    Output(my_table_sram, 'page_size'),
    Input(sram_test_name_drop, 'value'),
    Input(sram_row_drop, 'value'),)
def update_dropdown_options_sram(tname_v,sram_row_v):
    dff_S = sram_df_f.copy()
    if tname_v:
        dff_S =dff_S[dff_S.Test_Name==tname_v]
    return dff_S.to_dict('records'),sram_row_v
@callback(
    Output(my_table_fcb, 'data'),
    Output(my_table_fcb, 'page_size'),
    Input(fcb_test_name_drop, 'value'),
    Input(fcb_row_drop, 'value'),)
def update_dropdown_options_sram(tname_v,fcb_row_v):
    dff_F = fcb_df_f.copy()
    if tname_v:
        dff_F =dff_F[dff_F.Test_Name==tname_v]
    return dff_F.to_dict('records'),fcb_row_v



if __name__ == '__main__':
    app.run_server(debug=False, port = 8080)

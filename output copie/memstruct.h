/* This file was generate by EclipseMemstructGen.py*/
#ifndef MEMSTRUCT_H_
#define MEMSTRUCT_H_

#ifndef E92_EXCLUDE_MAIN_MEMSTRUCT

#include <stddef.h>

#include "can_cfg.h"
#include "can_sig.h"
#include "can_msg.h"
#include "can_frm.h"

#ifdef E92_USE_CUSTOM_MEMSTRUCT
       #include "custom_memstruct.h"
#endif
#include "service_can_callbacks.h"

#define CANFRM_EXTENDED_ID  (1<<29)
#define CANFRM_RTR          (1<<30)

/*Callback definition*/
/*******************************************************************/
/*      DRIVER      */
/********************************************************************/
#ifndef S_DRIVER_MOTOR_VELOCITY_callback
#        define S_DRIVER_MOTOR_VELOCITY_callback NULL
#endif
#ifndef S_DRIVER_MOTOR_CURRENT_callback
#        define S_DRIVER_MOTOR_CURRENT_callback NULL
#endif
#ifndef S_DRIVER_POWER_OFFSET_callback
#        define S_DRIVER_POWER_OFFSET_callback NULL
#endif
#ifndef S_DRIVER_BUS_CURRENT_callback
#        define S_DRIVER_BUS_CURRENT_callback NULL
#endif
/*******************************************************************/
/*      DRIVE      */
/********************************************************************/
#ifndef S_DRIVE_SERIAL_callback
#        define S_DRIVE_SERIAL_callback NULL
#endif
#ifndef S_DRIVE_ID_callback
#        define S_DRIVE_ID_callback NULL
#endif
#ifndef S_DRIVE_LIMIT_FLAGS_callback
#        define S_DRIVE_LIMIT_FLAGS_callback NULL
#endif
#ifndef S_DRIVE_ERR_FLAGS_callback
#        define S_DRIVE_ERR_FLAGS_callback NULL
#endif
#ifndef S_DRIVE_ACTIVE_MOTOR_callback
#        define S_DRIVE_ACTIVE_MOTOR_callback NULL
#endif
#ifndef S_DRIVE_TX_ERR_CNT_callback
#        define S_DRIVE_TX_ERR_CNT_callback NULL
#endif
#ifndef S_DRIVE_RX_ERR_CNT_callback
#        define S_DRIVE_RX_ERR_CNT_callback NULL
#endif
#ifndef S_DRIVE_BUS_VOLTAGE_callback
#        define S_DRIVE_BUS_VOLTAGE_callback NULL
#endif
#ifndef S_DRIVE_BUS_CURRENT_callback
#        define S_DRIVE_BUS_CURRENT_callback NULL
#endif
#ifndef S_DRIVE_MOTOR_VELOCITY_callback
#        define S_DRIVE_MOTOR_VELOCITY_callback NULL
#endif
#ifndef S_DRIVE_VEHICLE_VELOCITY_callback
#        define S_DRIVE_VEHICLE_VELOCITY_callback NULL
#endif
#ifndef S_DRIVE_PHASE_C_CURRENT_callback
#        define S_DRIVE_PHASE_C_CURRENT_callback NULL
#endif
#ifndef S_DRIVE_PHASE_B_CURRENT_callback
#        define S_DRIVE_PHASE_B_CURRENT_callback NULL
#endif
#ifndef S_DRIVE_BEMFQ_callback
#        define S_DRIVE_BEMFQ_callback NULL
#endif
#ifndef S_DRIVE_BEMFD_callback
#        define S_DRIVE_BEMFD_callback NULL
#endif
#ifndef S_DRIVE_15V_OFFSET_callback
#        define S_DRIVE_15V_OFFSET_callback NULL
#endif
#ifndef S_DRIVE_15V_callback
#        define S_DRIVE_15V_callback NULL
#endif
#ifndef S_DRIVE_1_9V_callback
#        define S_DRIVE_1_9V_callback NULL
#endif
#ifndef S_DRIVE_3_3V_callback
#        define S_DRIVE_3_3V_callback NULL
#endif
#ifndef S_DRIVE_MOTOR_TEMP_callback
#        define S_DRIVE_MOTOR_TEMP_callback NULL
#endif
#ifndef S_DRIVE_HEATSINK_TEMP_callback
#        define S_DRIVE_HEATSINK_TEMP_callback NULL
#endif
#ifndef S_DRIVE_DSP_TEMP_callback
#        define S_DRIVE_DSP_TEMP_callback NULL
#endif
#ifndef S_DRIVE_ODOMETER_callback
#        define S_DRIVE_ODOMETER_callback NULL
#endif
#ifndef S_DRIVE_DCBUS_AMPHOUR_callback
#        define S_DRIVE_DCBUS_AMPHOUR_callback NULL
#endif
/*******************************************************************/
/*      BMS      */
/********************************************************************/
#ifndef S_BMS_STATUS_callback
#        define S_BMS_STATUS_callback NULL
#endif
#ifndef S_BMS_OSTICK_callback
#        define S_BMS_OSTICK_callback NULL
#endif
#ifndef S_BMS_PACK_CURRENT_callback
#        define S_BMS_PACK_CURRENT_callback NULL
#endif
#ifndef S_BMS_PACK_VOLTAGE_callback
#        define S_BMS_PACK_VOLTAGE_callback NULL
#endif
#ifndef S_BMS_SUM_VOLTAGE_callback
#        define S_BMS_SUM_VOLTAGE_callback NULL
#endif
#ifndef S_BMS_AVERAGE_CELL_VOLTAGE_callback
#        define S_BMS_AVERAGE_CELL_VOLTAGE_callback NULL
#endif
#ifndef S_BMS_CELL_VOLTAGE_MAX_callback
#        define S_BMS_CELL_VOLTAGE_MAX_callback NULL
#endif
#ifndef S_BMS_CELL_HIGHEST_VOLTAGE_callback
#        define S_BMS_CELL_HIGHEST_VOLTAGE_callback NULL
#endif
#ifndef S_BMS_CELL_VOLTAGE_MIN_callback
#        define S_BMS_CELL_VOLTAGE_MIN_callback NULL
#endif
#ifndef S_BMS_CELL_LOWEST_VOLTAGE_callback
#        define S_BMS_CELL_LOWEST_VOLTAGE_callback NULL
#endif
#ifndef S_BMS_HIGHEST_TEMP_callback
#        define S_BMS_HIGHEST_TEMP_callback NULL
#endif
#ifndef S_BMS_LOWEST_TEMP_callback
#        define S_BMS_LOWEST_TEMP_callback NULL
#endif
#ifndef S_BMS_MASTER_TEMP_callback
#        define S_BMS_MASTER_TEMP_callback NULL
#endif
#ifndef S_BMS_IO_STATE_callback
#        define S_BMS_IO_STATE_callback NULL
#endif
#ifndef S_BMS_SYSTEM_STATE_callback
#        define S_BMS_SYSTEM_STATE_callback NULL
#endif
#ifndef S_BMS_ERRORS_FLAGS_callback
#        define S_BMS_ERRORS_FLAGS_callback NULL
#endif
#ifndef S_BMS_WARNING_FLAGS_callback
#        define S_BMS_WARNING_FLAGS_callback NULL
#endif
#ifndef S_BMS_SOC_callback
#        define S_BMS_SOC_callback NULL
#endif
#ifndef S_BMS_COULOMB_SOC_callback
#        define S_BMS_COULOMB_SOC_callback NULL
#endif
#ifndef S_BMS_AMP_H_SUM_callback
#        define S_BMS_AMP_H_SUM_callback NULL
#endif
#ifndef S_BMS_REMAINING_ENERGY_callback
#        define S_BMS_REMAINING_ENERGY_callback NULL
#endif
#ifndef S_BMS_SLAVE_COMM_WARNINGS_callback
#        define S_BMS_SLAVE_COMM_WARNINGS_callback NULL
#endif
#ifndef S_BMS_MASTER_POWER_UP_TIME_callback
#        define S_BMS_MASTER_POWER_UP_TIME_callback NULL
#endif
/*******************************************************************/
/*      DASHBOARD      */
/********************************************************************/
#ifndef S_DASHBOARD_STATUS_callback
#        define S_DASHBOARD_STATUS_callback NULL
#endif
#ifndef S_DASHBOARD_OSTICK_callback
#        define S_DASHBOARD_OSTICK_callback NULL
#endif
#ifndef S_DASHBOARD_BREAK_callback
#        define S_DASHBOARD_BREAK_callback NULL
#endif
#ifndef S_DASHBOARD_BUTTON_callback
#        define S_DASHBOARD_BUTTON_callback NULL
#endif
/*******************************************************************/
/*      TELEMETRIE      */
/********************************************************************/
#ifndef S_TELEMETRIE_STATUS_callback
#        define S_TELEMETRIE_STATUS_callback NULL
#endif
#ifndef S_TELEMETRIE_MODEM_ON_callback
#        define S_TELEMETRIE_MODEM_ON_callback NULL
#endif
#ifndef S_TELEMETRIE_XBEE_ON_callback
#        define S_TELEMETRIE_XBEE_ON_callback NULL
#endif
#ifndef S_TELEMETRIE_OSTICK_callback
#        define S_TELEMETRIE_OSTICK_callback NULL
#endif
/*******************************************************************/
/*      VOLANT      */
/********************************************************************/
#ifndef S_VOLANT_STATUS_callback
#        define S_VOLANT_STATUS_callback NULL
#endif
#ifndef S_VOLANT_OSTICK_callback
#        define S_VOLANT_OSTICK_callback NULL
#endif
#ifndef S_VOLANT_OPMODE_callback
#        define S_VOLANT_OPMODE_callback NULL
#endif
#ifndef S_VOLANT_BUTTON_callback
#        define S_VOLANT_BUTTON_callback NULL
#endif
/*******************************************************************/
/*      POWERSUPPLY      */
/********************************************************************/
#ifndef S_POWERSUPPLY_STATUS_callback
#        define S_POWERSUPPLY_STATUS_callback NULL
#endif
#ifndef S_POWERSUPPLY_OSTICK_callback
#        define S_POWERSUPPLY_OSTICK_callback NULL
#endif
#ifndef S_POWERSUPPLY_12V_CAN_COURANT_callback
#        define S_POWERSUPPLY_12V_CAN_COURANT_callback NULL
#endif
#ifndef S_POWERSUPPLY_12V_CAN_VOLTAGE_callback
#        define S_POWERSUPPLY_12V_CAN_VOLTAGE_callback NULL
#endif
#ifndef S_POWERSUPPLY_12V_HP_COURANT_callback
#        define S_POWERSUPPLY_12V_HP_COURANT_callback NULL
#endif
#ifndef S_POWERSUPPLY_12V_HP_VOLTAGE_callback
#        define S_POWERSUPPLY_12V_HP_VOLTAGE_callback NULL
#endif
#ifndef S_POWERSUPPLY_12V_AUX_COURANT_callback
#        define S_POWERSUPPLY_12V_AUX_COURANT_callback NULL
#endif
#ifndef S_POWERSUPPLY_12V_AUX_VOLTAGE_callback
#        define S_POWERSUPPLY_12V_AUX_VOLTAGE_callback NULL
#endif
/*******************************************************************/
/*      IGNITION      */
/********************************************************************/
#ifndef S_IGNITION_STATUS1_callback
#        define S_IGNITION_STATUS1_callback NULL
#endif
/*******************************************************************/
/*      FLASHER      */
/********************************************************************/
#ifndef S_FLASHER_1_STATUS_callback
#        define S_FLASHER_1_STATUS_callback NULL
#endif
#ifndef S_FLASHER_1_OSTICK_callback
#        define S_FLASHER_1_OSTICK_callback NULL
#endif
#ifndef S_FLASHER_2_STATUS_callback
#        define S_FLASHER_2_STATUS_callback NULL
#endif
#ifndef S_FLASHER_2_OSTICK_callback
#        define S_FLASHER_2_OSTICK_callback NULL
#endif
/*******************************************************************/
/*      MUPPET      */
/********************************************************************/
#ifndef S_MUPPET_FLAG_MPPT1_callback
#        define S_MUPPET_FLAG_MPPT1_callback NULL
#endif
#ifndef S_MUPPET_TEMP_MPPT1_callback
#        define S_MUPPET_TEMP_MPPT1_callback NULL
#endif
#ifndef S_MUPPET_IIN_MPPT1_callback
#        define S_MUPPET_IIN_MPPT1_callback NULL
#endif
#ifndef S_MUPPET_IOUT_MPPT1_callback
#        define S_MUPPET_IOUT_MPPT1_callback NULL
#endif
#ifndef S_MUPPET_UIN_MPPT1_callback
#        define S_MUPPET_UIN_MPPT1_callback NULL
#endif
#ifndef S_MUPPET_UOUT_MPPT1_callback
#        define S_MUPPET_UOUT_MPPT1_callback NULL
#endif
#ifndef S_MUPPET_FLAG_MPPT2_callback
#        define S_MUPPET_FLAG_MPPT2_callback NULL
#endif
#ifndef S_MUPPET_TEMP_MPPT2_callback
#        define S_MUPPET_TEMP_MPPT2_callback NULL
#endif
#ifndef S_MUPPET_IIN_MPPT2_callback
#        define S_MUPPET_IIN_MPPT2_callback NULL
#endif
#ifndef S_MUPPET_IOUT_MPPT2_callback
#        define S_MUPPET_IOUT_MPPT2_callback NULL
#endif
#ifndef S_MUPPET_UIN_MPPT2_callback
#        define S_MUPPET_UIN_MPPT2_callback NULL
#endif
#ifndef S_MUPPET_UOUT_MPPT2_callback
#        define S_MUPPET_UOUT_MPPT2_callback NULL
#endif
#ifndef S_MUPPET_FLAG_MPPT3_callback
#        define S_MUPPET_FLAG_MPPT3_callback NULL
#endif
#ifndef S_MUPPET_TEMP_MPPT3_callback
#        define S_MUPPET_TEMP_MPPT3_callback NULL
#endif
#ifndef S_MUPPET_IIN_MPPT3_callback
#        define S_MUPPET_IIN_MPPT3_callback NULL
#endif
#ifndef S_MUPPET_IOUT_MPPT3_callback
#        define S_MUPPET_IOUT_MPPT3_callback NULL
#endif
#ifndef S_MUPPET_UIN_MPPT3_callback
#        define S_MUPPET_UIN_MPPT3_callback NULL
#endif
#ifndef S_MUPPET_UOUT_MPPT3_callback
#        define S_MUPPET_UOUT_MPPT3_callback NULL
#endif
#ifndef S_MUPPET_FLAG_MPPT4_callback
#        define S_MUPPET_FLAG_MPPT4_callback NULL
#endif
#ifndef S_MUPPET_TEMP_MPPT4_callback
#        define S_MUPPET_TEMP_MPPT4_callback NULL
#endif
#ifndef S_MUPPET_IIN_MPPT4_callback
#        define S_MUPPET_IIN_MPPT4_callback NULL
#endif
#ifndef S_MUPPET_IOUT_MPPT4_callback
#        define S_MUPPET_IOUT_MPPT4_callback NULL
#endif
#ifndef S_MUPPET_UIN_MPPT4_callback
#        define S_MUPPET_UIN_MPPT4_callback NULL
#endif
#ifndef S_MUPPET_UOUT_MPPT4_callback
#        define S_MUPPET_UOUT_MPPT4_callback NULL
#endif
/*******************************************************************/
/*      TEMPLATE      */
/********************************************************************/
#ifndef S_TEMPLATE_STATUS_callback
#        define S_TEMPLATE_STATUS_callback NULL
#endif
#ifndef S_TEMPLATE_OSTICK_callback
#        define S_TEMPLATE_OSTICK_callback NULL
#endif
#ifndef S_TEMPLATE_LED_callback
#        define S_TEMPLATE_LED_callback NULL
#endif
/*Board enum*/
enum{
        ID_OFFSET_DRIVER = 0x100,
        ID_OFFSET_DRIVE = 0x200,
        ID_OFFSET_BMS = 0x300L | CANFRM_EXTENDED_ID,
        ID_OFFSET_DASHBOARD = 0x400L | CANFRM_EXTENDED_ID,
        ID_OFFSET_TELEMETRIE = 0x500L | CANFRM_EXTENDED_ID,
        ID_OFFSET_VOLANT = 0x600L | CANFRM_EXTENDED_ID,
        ID_OFFSET_POWERSUPPLY = 0x700L | CANFRM_EXTENDED_ID,
        ID_OFFSET_IGNITION = 0x800L | CANFRM_EXTENDED_ID,
        ID_OFFSET_FLASHER = 0x900L | CANFRM_EXTENDED_ID,
        ID_OFFSET_MUPPET = 0x1000L | CANFRM_EXTENDED_ID,
        ID_OFFSET_TEMPLATE = 0xFFFFL | CANFRM_EXTENDED_ID,
};
/*Signal enum*/
enum{
/*******************************************************************/
/*      DRIVER      */
/********************************************************************/
        S_DRIVER_MOTOR_VELOCITY,
        S_DRIVER_MOTOR_CURRENT,
        S_DRIVER_POWER_OFFSET,
        S_DRIVER_BUS_CURRENT,
/*******************************************************************/
/*      DRIVE      */
/********************************************************************/
        S_DRIVE_SERIAL,
        S_DRIVE_ID,
        S_DRIVE_LIMIT_FLAGS,
        S_DRIVE_ERR_FLAGS,
        S_DRIVE_ACTIVE_MOTOR,
        S_DRIVE_TX_ERR_CNT,
        S_DRIVE_RX_ERR_CNT,
        S_DRIVE_BUS_VOLTAGE,
        S_DRIVE_BUS_CURRENT,
        S_DRIVE_MOTOR_VELOCITY,
        S_DRIVE_VEHICLE_VELOCITY,
        S_DRIVE_PHASE_C_CURRENT,
        S_DRIVE_PHASE_B_CURRENT,
        S_DRIVE_BEMFQ,
        S_DRIVE_BEMFD,
        S_DRIVE_15V_OFFSET,
        S_DRIVE_15V,
        S_DRIVE_1_9V,
        S_DRIVE_3_3V,
        S_DRIVE_MOTOR_TEMP,
        S_DRIVE_HEATSINK_TEMP,
        S_DRIVE_DSP_TEMP,
        S_DRIVE_ODOMETER,
        S_DRIVE_DCBUS_AMPHOUR,
/*******************************************************************/
/*      BMS      */
/********************************************************************/
        S_BMS_STATUS,
        S_BMS_OSTICK,
        S_BMS_PACK_CURRENT,
        S_BMS_PACK_VOLTAGE,
        S_BMS_SUM_VOLTAGE,
        S_BMS_AVERAGE_CELL_VOLTAGE,
        S_BMS_CELL_VOLTAGE_MAX,
        S_BMS_CELL_HIGHEST_VOLTAGE,
        S_BMS_CELL_VOLTAGE_MIN,
        S_BMS_CELL_LOWEST_VOLTAGE,
        S_BMS_HIGHEST_TEMP,
        S_BMS_LOWEST_TEMP,
        S_BMS_MASTER_TEMP,
        S_BMS_IO_STATE,
        S_BMS_SYSTEM_STATE,
        S_BMS_ERRORS_FLAGS,
        S_BMS_WARNING_FLAGS,
        S_BMS_SOC,
        S_BMS_COULOMB_SOC,
        S_BMS_AMP_H_SUM,
        S_BMS_REMAINING_ENERGY,
        S_BMS_SLAVE_COMM_WARNINGS,
        S_BMS_MASTER_POWER_UP_TIME,
/*******************************************************************/
/*      DASHBOARD      */
/********************************************************************/
        S_DASHBOARD_STATUS,
        S_DASHBOARD_OSTICK,
        S_DASHBOARD_BREAK,
        S_DASHBOARD_BUTTON,
/*******************************************************************/
/*      TELEMETRIE      */
/********************************************************************/
        S_TELEMETRIE_STATUS,
        S_TELEMETRIE_MODEM_ON,
        S_TELEMETRIE_XBEE_ON,
        S_TELEMETRIE_OSTICK,
/*******************************************************************/
/*      VOLANT      */
/********************************************************************/
        S_VOLANT_STATUS,
        S_VOLANT_OSTICK,
        S_VOLANT_OPMODE,
        S_VOLANT_BUTTON,
/*******************************************************************/
/*      POWERSUPPLY      */
/********************************************************************/
        S_POWERSUPPLY_STATUS,
        S_POWERSUPPLY_OSTICK,
        S_POWERSUPPLY_12V_CAN_COURANT,
        S_POWERSUPPLY_12V_CAN_VOLTAGE,
        S_POWERSUPPLY_12V_HP_COURANT,
        S_POWERSUPPLY_12V_HP_VOLTAGE,
        S_POWERSUPPLY_12V_AUX_COURANT,
        S_POWERSUPPLY_12V_AUX_VOLTAGE,
/*******************************************************************/
/*      IGNITION      */
/********************************************************************/
        S_IGNITION_STATUS1,
/*******************************************************************/
/*      FLASHER      */
/********************************************************************/
        S_FLASHER_1_STATUS,
        S_FLASHER_1_OSTICK,
        S_FLASHER_2_STATUS,
        S_FLASHER_2_OSTICK,
/*******************************************************************/
/*      MUPPET      */
/********************************************************************/
        S_MUPPET_FLAG_MPPT1,
        S_MUPPET_TEMP_MPPT1,
        S_MUPPET_IIN_MPPT1,
        S_MUPPET_IOUT_MPPT1,
        S_MUPPET_UIN_MPPT1,
        S_MUPPET_UOUT_MPPT1,
        S_MUPPET_FLAG_MPPT2,
        S_MUPPET_TEMP_MPPT2,
        S_MUPPET_IIN_MPPT2,
        S_MUPPET_IOUT_MPPT2,
        S_MUPPET_UIN_MPPT2,
        S_MUPPET_UOUT_MPPT2,
        S_MUPPET_FLAG_MPPT3,
        S_MUPPET_TEMP_MPPT3,
        S_MUPPET_IIN_MPPT3,
        S_MUPPET_IOUT_MPPT3,
        S_MUPPET_UIN_MPPT3,
        S_MUPPET_UOUT_MPPT3,
        S_MUPPET_FLAG_MPPT4,
        S_MUPPET_TEMP_MPPT4,
        S_MUPPET_IIN_MPPT4,
        S_MUPPET_IOUT_MPPT4,
        S_MUPPET_UIN_MPPT4,
        S_MUPPET_UOUT_MPPT4,
/*******************************************************************/
/*      TEMPLATE      */
/********************************************************************/
        S_TEMPLATE_STATUS,
        S_TEMPLATE_OSTICK,
        S_TEMPLATE_LED,

#ifdef E92_USE_CUSTOM_MEMSTRUCT
        S_CUSTOM_SIGNALS_ID
#endif
};
/*Message enum*/
enum{
/*******************************************************************/
/*      DRIVER      */
/********************************************************************/
        M_DRIVER_MOTOR_CMD = 1,
        M_DRIVER_POWER_CMD,
        M_MAX_DRIVER = 2,
/*******************************************************************/
/*      DRIVE      */
/********************************************************************/
        M_DRIVE_ID = 0,
        M_DRIVE_STATUS,
        M_DRIVE_BUS,
        M_DRIVE_VELOCITY,
        M_DRIVE_PHASE_CURRENT,
        M_DRIVE_BEMF = 7,
        M_DRIVE_15V,
        M_DRIVE_33V_19V,
        M_DRIVE_HEATSINK_MOTOR_TEMP = 11,
        M_DRIVE_DSP_TEMP,
        M_DRIVE_ODOMETER_AMPHOUR = 14,
        M_MAX_DRIVE = 11,
/*******************************************************************/
/*      BMS      */
/********************************************************************/
        M_BMS_STATUS = 0,
        M_BMS_CURRENT,
        M_BMS_VOLTAGE,
        M_BMS_CELL_VOLTAGE,
        M_BMS_TEMP,
        M_BMS_STATE,
        M_BMS_ERRORS,
        M_BMS_CAPACITY,
        M_BMS_DATA,
        M_MAX_BMS = 9,
/*******************************************************************/
/*      DASHBOARD      */
/********************************************************************/
        M_DASHBOARD_STATUS = 0,
        M_DASHBOARD_CTRL,
        M_MAX_DASHBOARD = 2,
/*******************************************************************/
/*      TELEMETRIE      */
/********************************************************************/
        M_TELEMETRIE_STATUS = 0,
        M_MAX_TELEMETRIE = 1,
/*******************************************************************/
/*      VOLANT      */
/********************************************************************/
        M_VOLANT_STATUS = 0,
        M_VOLANT_CTRL,
        M_MAX_VOLANT = 2,
/*******************************************************************/
/*      POWERSUPPLY      */
/********************************************************************/
        M_POWERSUPPLY_STATUS = 0,
        M_POWERSUPPLY_CAN,
        M_POWERSUPPLY_HP,
        M_POWERSUPPLY_AUX,
        M_MAX_POWERSUPPLY = 4,
/*******************************************************************/
/*      IGNITION      */
/********************************************************************/
        M_IGNITION_ID = 0,
        M_MAX_IGNITION = 1,
/*******************************************************************/
/*      FLASHER      */
/********************************************************************/
        M_FLASHER_TOP = 0,
        M_FLASHER_BOT,
        M_MAX_FLASHER = 2,
/*******************************************************************/
/*      MUPPET      */
/********************************************************************/
        M_MUPPET_STATUS_MPPT1 = 0,
        M_MUPPET_I_MPPT1,
        M_MUPPET_U_MPPT1,
        M_MUPPET_STATUS_MPPT2,
        M_MUPPET_I_MPPT2,
        M_MUPPET_U_MPPT2,
        M_MUPPET_STATUS_MPPT3,
        M_MUPPET_I_MPPT3,
        M_MUPPET_U_MPPT3,
        M_MUPPET_STATUS_MPPT4,
        M_MUPPET_I_MPPT4,
        M_MUPPET_U_MPPT4,
        M_MAX_MUPPET = 12,
/*******************************************************************/
/*      TEMPLATE      */
/********************************************************************/
        TEMPLATE_STATUS = 0,
        M_MAX_TEMPLATE = 1,
};

#define M_MAX                 47

#endif /*E92_EXCLUDE_MAIN_MEMSTRUCT*/
#endif

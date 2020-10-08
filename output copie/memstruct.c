/* This file was generate by EclipseMemstructGen.py*/
#ifndef E92_EXCLUDE_MAIN_MEMSTRUCT

#include <stdint.h>

#include "can_sig.h"
#include "can_msg.h"

#include "memstruct.h"

#ifdef E92_USE_CUSTOM_MEMSTRUCT
    #include "custom_memstruct.h"
#endif

#define CAN_PARA_MACRO(signame, width, initValue, callback) { CANSIG_UNCHANGED, width, initValue, callback }

CANSIG_DATA CanSigTbl[CANSIG_N];
const CANSIG_PARA CanSig[CANSIG_N] = {
/*******************************************************************/
/*      DRIVER      */
/********************************************************************/
        CAN_PARA_MACRO(S_DRIVER_MOTOR_VELOCITY, sizeof(float), 0, S_DRIVER_MOTOR_VELOCITY_callback),
        CAN_PARA_MACRO(S_DRIVER_MOTOR_CURRENT, sizeof(float), 0, S_DRIVER_MOTOR_CURRENT_callback),
        CAN_PARA_MACRO(S_DRIVER_POWER_OFFSET, sizeof(uint32_t), 0, S_DRIVER_POWER_OFFSET_callback),
        CAN_PARA_MACRO(S_DRIVER_BUS_CURRENT, sizeof(float), 0, S_DRIVER_BUS_CURRENT_callback),
/*******************************************************************/
/*      DRIVE      */
/********************************************************************/
        CAN_PARA_MACRO(S_DRIVE_SERIAL, sizeof(uint32_t), 0, S_DRIVE_SERIAL_callback),
        CAN_PARA_MACRO(S_DRIVE_ID, sizeof(uint32_t), 0, S_DRIVE_ID_callback),
        CAN_PARA_MACRO(S_DRIVE_LIMIT_FLAGS, sizeof(uint16_t), 0, S_DRIVE_LIMIT_FLAGS_callback),
        CAN_PARA_MACRO(S_DRIVE_ERR_FLAGS, sizeof(uint16_t), 0, S_DRIVE_ERR_FLAGS_callback),
        CAN_PARA_MACRO(S_DRIVE_ACTIVE_MOTOR, sizeof(uint16_t), 0, S_DRIVE_ACTIVE_MOTOR_callback),
        CAN_PARA_MACRO(S_DRIVE_TX_ERR_CNT, sizeof(uint8_t), 0, S_DRIVE_TX_ERR_CNT_callback),
        CAN_PARA_MACRO(S_DRIVE_RX_ERR_CNT, sizeof(uint8_t), 0, S_DRIVE_RX_ERR_CNT_callback),
        CAN_PARA_MACRO(S_DRIVE_BUS_VOLTAGE, sizeof(float), 0, S_DRIVE_BUS_VOLTAGE_callback),
        CAN_PARA_MACRO(S_DRIVE_BUS_CURRENT, sizeof(float), 0, S_DRIVE_BUS_CURRENT_callback),
        CAN_PARA_MACRO(S_DRIVE_MOTOR_VELOCITY, sizeof(float), 0, S_DRIVE_MOTOR_VELOCITY_callback),
        CAN_PARA_MACRO(S_DRIVE_VEHICLE_VELOCITY, sizeof(float), 0, S_DRIVE_VEHICLE_VELOCITY_callback),
        CAN_PARA_MACRO(S_DRIVE_PHASE_C_CURRENT, sizeof(float), 0, S_DRIVE_PHASE_C_CURRENT_callback),
        CAN_PARA_MACRO(S_DRIVE_PHASE_B_CURRENT, sizeof(float), 0, S_DRIVE_PHASE_B_CURRENT_callback),
        CAN_PARA_MACRO(S_DRIVE_BEMFQ, sizeof(float), 0, S_DRIVE_BEMFQ_callback),
        CAN_PARA_MACRO(S_DRIVE_BEMFD, sizeof(float), 0, S_DRIVE_BEMFD_callback),
        CAN_PARA_MACRO(S_DRIVE_15V_OFFSET, sizeof(float), 0, S_DRIVE_15V_OFFSET_callback),
        CAN_PARA_MACRO(S_DRIVE_15V, sizeof(float), 0, S_DRIVE_15V_callback),
        CAN_PARA_MACRO(S_DRIVE_1_9V, sizeof(float), 0, S_DRIVE_1_9V_callback),
        CAN_PARA_MACRO(S_DRIVE_3_3V, sizeof(float), 0, S_DRIVE_3_3V_callback),
        CAN_PARA_MACRO(S_DRIVE_MOTOR_TEMP, sizeof(float), 0, S_DRIVE_MOTOR_TEMP_callback),
        CAN_PARA_MACRO(S_DRIVE_HEATSINK_TEMP, sizeof(float), 0, S_DRIVE_HEATSINK_TEMP_callback),
        CAN_PARA_MACRO(S_DRIVE_DSP_TEMP, sizeof(float), 0, S_DRIVE_DSP_TEMP_callback),
        CAN_PARA_MACRO(S_DRIVE_ODOMETER, sizeof(float), 0, S_DRIVE_ODOMETER_callback),
        CAN_PARA_MACRO(S_DRIVE_DCBUS_AMPHOUR, sizeof(float), 0, S_DRIVE_DCBUS_AMPHOUR_callback),
/*******************************************************************/
/*      BMS      */
/********************************************************************/
        CAN_PARA_MACRO(S_BMS_STATUS, sizeof(uint16_t), 0, S_BMS_STATUS_callback),
        CAN_PARA_MACRO(S_BMS_OSTICK, sizeof(uint32_t), 0, S_BMS_OSTICK_callback),
        CAN_PARA_MACRO(S_BMS_PACK_CURRENT, sizeof(int32_t), 0, S_BMS_PACK_CURRENT_callback),
        CAN_PARA_MACRO(S_BMS_PACK_VOLTAGE, sizeof(uint16_t), 0, S_BMS_PACK_VOLTAGE_callback),
        CAN_PARA_MACRO(S_BMS_SUM_VOLTAGE, sizeof(uint16_t), 0, S_BMS_SUM_VOLTAGE_callback),
        CAN_PARA_MACRO(S_BMS_AVERAGE_CELL_VOLTAGE, sizeof(uint16_t), 0, S_BMS_AVERAGE_CELL_VOLTAGE_callback),
        CAN_PARA_MACRO(S_BMS_CELL_VOLTAGE_MAX, sizeof(uint16_t), 0, S_BMS_CELL_VOLTAGE_MAX_callback),
        CAN_PARA_MACRO(S_BMS_CELL_HIGHEST_VOLTAGE, sizeof(uint8_t), 0, S_BMS_CELL_HIGHEST_VOLTAGE_callback),
        CAN_PARA_MACRO(S_BMS_CELL_VOLTAGE_MIN, sizeof(uint16_t), 0, S_BMS_CELL_VOLTAGE_MIN_callback),
        CAN_PARA_MACRO(S_BMS_CELL_LOWEST_VOLTAGE, sizeof(uint8_t), 0, S_BMS_CELL_LOWEST_VOLTAGE_callback),
        CAN_PARA_MACRO(S_BMS_HIGHEST_TEMP, sizeof(uint16_t), 0, S_BMS_HIGHEST_TEMP_callback),
        CAN_PARA_MACRO(S_BMS_LOWEST_TEMP, sizeof(uint16_t), 0, S_BMS_LOWEST_TEMP_callback),
        CAN_PARA_MACRO(S_BMS_MASTER_TEMP, sizeof(uint16_t), 0, S_BMS_MASTER_TEMP_callback),
        CAN_PARA_MACRO(S_BMS_IO_STATE, sizeof(uint8_t), 0, S_BMS_IO_STATE_callback),
        CAN_PARA_MACRO(S_BMS_SYSTEM_STATE, sizeof(uint8_t), 0, S_BMS_SYSTEM_STATE_callback),
        CAN_PARA_MACRO(S_BMS_ERRORS_FLAGS, sizeof(uint32_t), 0, S_BMS_ERRORS_FLAGS_callback),
        CAN_PARA_MACRO(S_BMS_WARNING_FLAGS, sizeof(uint32_t), 0, S_BMS_WARNING_FLAGS_callback),
        CAN_PARA_MACRO(S_BMS_SOC, sizeof(uint8_t), 0, S_BMS_SOC_callback),
        CAN_PARA_MACRO(S_BMS_COULOMB_SOC, sizeof(uint8_t), 0, S_BMS_COULOMB_SOC_callback),
        CAN_PARA_MACRO(S_BMS_AMP_H_SUM, sizeof(uint16_t), 0, S_BMS_AMP_H_SUM_callback),
        CAN_PARA_MACRO(S_BMS_REMAINING_ENERGY, sizeof(uint16_t), 0, S_BMS_REMAINING_ENERGY_callback),
        CAN_PARA_MACRO(S_BMS_SLAVE_COMM_WARNINGS, sizeof(uint32_t), 0, S_BMS_SLAVE_COMM_WARNINGS_callback),
        CAN_PARA_MACRO(S_BMS_MASTER_POWER_UP_TIME, sizeof(uint32_t), 0, S_BMS_MASTER_POWER_UP_TIME_callback),
/*******************************************************************/
/*      DASHBOARD      */
/********************************************************************/
        CAN_PARA_MACRO(S_DASHBOARD_STATUS, sizeof(uint16_t), 0, S_DASHBOARD_STATUS_callback),
        CAN_PARA_MACRO(S_DASHBOARD_OSTICK, sizeof(uint32_t), 0, S_DASHBOARD_OSTICK_callback),
        CAN_PARA_MACRO(S_DASHBOARD_BREAK, sizeof(uint8_t), 0, S_DASHBOARD_BREAK_callback),
        CAN_PARA_MACRO(S_DASHBOARD_BUTTON, sizeof(uint8_t), 0, S_DASHBOARD_BUTTON_callback),
/*******************************************************************/
/*      TELEMETRIE      */
/********************************************************************/
        CAN_PARA_MACRO(S_TELEMETRIE_STATUS, sizeof(uint16_t), 0, S_TELEMETRIE_STATUS_callback),
        CAN_PARA_MACRO(S_TELEMETRIE_MODEM_ON, sizeof(uint8_t), 0, S_TELEMETRIE_MODEM_ON_callback),
        CAN_PARA_MACRO(S_TELEMETRIE_XBEE_ON, sizeof(uint8_t), 0, S_TELEMETRIE_XBEE_ON_callback),
        CAN_PARA_MACRO(S_TELEMETRIE_OSTICK, sizeof(uint32_t), 0, S_TELEMETRIE_OSTICK_callback),
/*******************************************************************/
/*      VOLANT      */
/********************************************************************/
        CAN_PARA_MACRO(S_VOLANT_STATUS, sizeof(uint16_t), 0, S_VOLANT_STATUS_callback),
        CAN_PARA_MACRO(S_VOLANT_OSTICK, sizeof(uint32_t), 0, S_VOLANT_OSTICK_callback),
        CAN_PARA_MACRO(S_VOLANT_OPMODE, sizeof(uint8_t), 0, S_VOLANT_OPMODE_callback),
        CAN_PARA_MACRO(S_VOLANT_BUTTON, sizeof(uint16_t), 0, S_VOLANT_BUTTON_callback),
/*******************************************************************/
/*      POWERSUPPLY      */
/********************************************************************/
        CAN_PARA_MACRO(S_POWERSUPPLY_STATUS, sizeof(uint16_t), 0, S_POWERSUPPLY_STATUS_callback),
        CAN_PARA_MACRO(S_POWERSUPPLY_OSTICK, sizeof(uint32_t), 0, S_POWERSUPPLY_OSTICK_callback),
        CAN_PARA_MACRO(S_POWERSUPPLY_12V_CAN_COURANT, sizeof(int16_t), 3, S_POWERSUPPLY_12V_CAN_COURANT_callback),
        CAN_PARA_MACRO(S_POWERSUPPLY_12V_CAN_VOLTAGE, sizeof(int16_t), 3, S_POWERSUPPLY_12V_CAN_VOLTAGE_callback),
        CAN_PARA_MACRO(S_POWERSUPPLY_12V_HP_COURANT, sizeof(int16_t), 3, S_POWERSUPPLY_12V_HP_COURANT_callback),
        CAN_PARA_MACRO(S_POWERSUPPLY_12V_HP_VOLTAGE, sizeof(int16_t), 3, S_POWERSUPPLY_12V_HP_VOLTAGE_callback),
        CAN_PARA_MACRO(S_POWERSUPPLY_12V_AUX_COURANT, sizeof(int16_t), 3, S_POWERSUPPLY_12V_AUX_COURANT_callback),
        CAN_PARA_MACRO(S_POWERSUPPLY_12V_AUX_VOLTAGE, sizeof(int16_t), 3, S_POWERSUPPLY_12V_AUX_VOLTAGE_callback),
/*******************************************************************/
/*      IGNITION      */
/********************************************************************/
        CAN_PARA_MACRO(S_IGNITION_STATUS1, sizeof(uint8_t), 0, S_IGNITION_STATUS1_callback),
/*******************************************************************/
/*      FLASHER      */
/********************************************************************/
        CAN_PARA_MACRO(S_FLASHER_1_STATUS, sizeof(uint16_t), 0, S_FLASHER_1_STATUS_callback),
        CAN_PARA_MACRO(S_FLASHER_1_OSTICK, sizeof(uint32_t), 0, S_FLASHER_1_OSTICK_callback),
        CAN_PARA_MACRO(S_FLASHER_2_STATUS, sizeof(uint16_t), 0, S_FLASHER_2_STATUS_callback),
        CAN_PARA_MACRO(S_FLASHER_2_OSTICK, sizeof(uint32_t), 0, S_FLASHER_2_OSTICK_callback),
/*******************************************************************/
/*      MUPPET      */
/********************************************************************/
        CAN_PARA_MACRO(S_MUPPET_FLAG_MPPT1, sizeof(uint8_t), 0, S_MUPPET_FLAG_MPPT1_callback),
        CAN_PARA_MACRO(S_MUPPET_TEMP_MPPT1, sizeof(uint8_t), 0, S_MUPPET_TEMP_MPPT1_callback),
        CAN_PARA_MACRO(S_MUPPET_IIN_MPPT1, sizeof(float), 0, S_MUPPET_IIN_MPPT1_callback),
        CAN_PARA_MACRO(S_MUPPET_IOUT_MPPT1, sizeof(float), 0, S_MUPPET_IOUT_MPPT1_callback),
        CAN_PARA_MACRO(S_MUPPET_UIN_MPPT1, sizeof(float), 0, S_MUPPET_UIN_MPPT1_callback),
        CAN_PARA_MACRO(S_MUPPET_UOUT_MPPT1, sizeof(float), 0, S_MUPPET_UOUT_MPPT1_callback),
        CAN_PARA_MACRO(S_MUPPET_FLAG_MPPT2, sizeof(uint8_t), 0, S_MUPPET_FLAG_MPPT2_callback),
        CAN_PARA_MACRO(S_MUPPET_TEMP_MPPT2, sizeof(uint8_t), 0, S_MUPPET_TEMP_MPPT2_callback),
        CAN_PARA_MACRO(S_MUPPET_IIN_MPPT2, sizeof(float), 0, S_MUPPET_IIN_MPPT2_callback),
        CAN_PARA_MACRO(S_MUPPET_IOUT_MPPT2, sizeof(float), 0, S_MUPPET_IOUT_MPPT2_callback),
        CAN_PARA_MACRO(S_MUPPET_UIN_MPPT2, sizeof(float), 0, S_MUPPET_UIN_MPPT2_callback),
        CAN_PARA_MACRO(S_MUPPET_UOUT_MPPT2, sizeof(float), 0, S_MUPPET_UOUT_MPPT2_callback),
        CAN_PARA_MACRO(S_MUPPET_FLAG_MPPT3, sizeof(uint8_t), 0, S_MUPPET_FLAG_MPPT3_callback),
        CAN_PARA_MACRO(S_MUPPET_TEMP_MPPT3, sizeof(uint8_t), 0, S_MUPPET_TEMP_MPPT3_callback),
        CAN_PARA_MACRO(S_MUPPET_IIN_MPPT3, sizeof(float), 0, S_MUPPET_IIN_MPPT3_callback),
        CAN_PARA_MACRO(S_MUPPET_IOUT_MPPT3, sizeof(float), 0, S_MUPPET_IOUT_MPPT3_callback),
        CAN_PARA_MACRO(S_MUPPET_UIN_MPPT3, sizeof(float), 0, S_MUPPET_UIN_MPPT3_callback),
        CAN_PARA_MACRO(S_MUPPET_UOUT_MPPT3, sizeof(float), 0, S_MUPPET_UOUT_MPPT3_callback),
        CAN_PARA_MACRO(S_MUPPET_FLAG_MPPT4, sizeof(uint8_t), 0, S_MUPPET_FLAG_MPPT4_callback),
        CAN_PARA_MACRO(S_MUPPET_TEMP_MPPT4, sizeof(uint8_t), 0, S_MUPPET_TEMP_MPPT4_callback),
        CAN_PARA_MACRO(S_MUPPET_IIN_MPPT4, sizeof(float), 0, S_MUPPET_IIN_MPPT4_callback),
        CAN_PARA_MACRO(S_MUPPET_IOUT_MPPT4, sizeof(float), 0, S_MUPPET_IOUT_MPPT4_callback),
        CAN_PARA_MACRO(S_MUPPET_UIN_MPPT4, sizeof(float), 0, S_MUPPET_UIN_MPPT4_callback),
        CAN_PARA_MACRO(S_MUPPET_UOUT_MPPT4, sizeof(float), 0, S_MUPPET_UOUT_MPPT4_callback),
/*******************************************************************/
/*      TEMPLATE      */
/********************************************************************/
        CAN_PARA_MACRO(S_TEMPLATE_STATUS, sizeof(uint16_t), 0, S_TEMPLATE_STATUS_callback),
        CAN_PARA_MACRO(S_TEMPLATE_OSTICK, sizeof(uint32_t), 0, S_TEMPLATE_OSTICK_callback),
        CAN_PARA_MACRO(S_TEMPLATE_LED, sizeof(uint8_t), 0, S_TEMPLATE_LED_callback),

#ifdef E92_USE_CUSTOM_MEMSTRUCT
/*******************************************************************/
/*                                                    CUSTOM CAN                                                         */
/********************************************************************/
        CUSTOM_CAN_SIG,
#endif

};

#ifndef M_DRIVER_TXRX
#        define M_DRIVER_TXRX CANMSG_RX
#endif
#ifndef M_DRIVE_TXRX
#        define M_DRIVE_TXRX CANMSG_RX
#endif
#ifndef M_BMS_TXRX
#        define M_BMS_TXRX CANMSG_RX
#endif
#ifndef M_DASHBOARD_TXRX
#        define M_DASHBOARD_TXRX CANMSG_RX
#endif
#ifndef M_TELEMETRIE_TXRX
#        define M_TELEMETRIE_TXRX CANMSG_RX
#endif
#ifndef M_VOLANT_TXRX
#        define M_VOLANT_TXRX CANMSG_RX
#endif
#ifndef M_POWERSUPPLY_TXRX
#        define M_POWERSUPPLY_TXRX CANMSG_RX
#endif
#ifndef M_IGNITION_TXRX
#        define M_IGNITION_TXRX CANMSG_RX
#endif
#ifndef M_FLASHER_TXRX
#        define M_FLASHER_TXRX CANMSG_RX
#endif
#ifndef M_MUPPET_TXRX
#        define M_MUPPET_TXRX CANMSG_RX
#endif
#ifndef M_TEMPLATE_TXRX
#        define M_TEMPLATE_TXRX CANMSG_RX
#endif


const CANMSG_PARA CanMsg[CANMSG_N] = {
/*******************************************************************/
/*      DRIVER      */
/********************************************************************/
        {
                ID_OFFSET_DRIVER + M_DRIVER_MOTOR_CMD, /* CAN-Identifier */
                M_DRIVER_TXRX, /* Message Type */
                sizeof(float) + sizeof(float), /* DLC of Message */
                2, /* No. of Links */
                {
                        {
                                S_DRIVER_MOTOR_VELOCITY,       /* Signal ID */
(                                0)|(CANFRM_LITTLE_ENDIAN)                                       /* Byte Position */
                        },
                        {
                                S_DRIVER_MOTOR_CURRENT,       /* Signal ID */
(                                0 + sizeof(float))|(CANFRM_LITTLE_ENDIAN)                                       /* Byte Position */
                        }
                }
        },
        {
                ID_OFFSET_DRIVER + M_DRIVER_POWER_CMD, /* CAN-Identifier */
                M_DRIVER_TXRX, /* Message Type */
                sizeof(uint32_t) + sizeof(float), /* DLC of Message */
                2, /* No. of Links */
                {
                        {
                                S_DRIVER_POWER_OFFSET,       /* Signal ID */
(                                0)|(CANFRM_LITTLE_ENDIAN)                                       /* Byte Position */
                        },
                        {
                                S_DRIVER_BUS_CURRENT,       /* Signal ID */
(                                0 + sizeof(uint32_t))|(CANFRM_LITTLE_ENDIAN)                                       /* Byte Position */
                        }
                }
        },
/*******************************************************************/
/*      DRIVE      */
/********************************************************************/
        {
                ID_OFFSET_DRIVE + M_DRIVE_ID, /* CAN-Identifier */
                M_DRIVE_TXRX, /* Message Type */
                sizeof(uint32_t) + sizeof(uint32_t), /* DLC of Message */
                2, /* No. of Links */
                {
                        {
                                S_DRIVE_SERIAL,       /* Signal ID */
(                                0)|(CANFRM_LITTLE_ENDIAN)                                       /* Byte Position */
                        },
                        {
                                S_DRIVE_ID,       /* Signal ID */
(                                0 + sizeof(uint32_t))|(CANFRM_LITTLE_ENDIAN)                                       /* Byte Position */
                        }
                }
        },
        {
                ID_OFFSET_DRIVE + M_DRIVE_STATUS, /* CAN-Identifier */
                M_DRIVE_TXRX, /* Message Type */
                sizeof(uint16_t) + sizeof(uint16_t) + sizeof(uint16_t) + sizeof(uint8_t) + sizeof(uint8_t), /* DLC of Message */
                5, /* No. of Links */
                {
                        {
                                S_DRIVE_LIMIT_FLAGS,       /* Signal ID */
(                                0)|(CANFRM_LITTLE_ENDIAN)                                       /* Byte Position */
                        },
                        {
                                S_DRIVE_ERR_FLAGS,       /* Signal ID */
(                                0 + sizeof(uint16_t))|(CANFRM_LITTLE_ENDIAN)                                       /* Byte Position */
                        },
                        {
                                S_DRIVE_ACTIVE_MOTOR,       /* Signal ID */
(                                0 + sizeof(uint16_t) + sizeof(uint16_t))|(CANFRM_LITTLE_ENDIAN)                                       /* Byte Position */
                        },
                        {
                                S_DRIVE_TX_ERR_CNT,       /* Signal ID */
(                                0 + sizeof(uint16_t) + sizeof(uint16_t) + sizeof(uint16_t))|(CANFRM_LITTLE_ENDIAN)                                       /* Byte Position */
                        },
                        {
                                S_DRIVE_RX_ERR_CNT,       /* Signal ID */
(                                0 + sizeof(uint16_t) + sizeof(uint16_t) + sizeof(uint16_t) + sizeof(uint8_t))|(CANFRM_LITTLE_ENDIAN)                                       /* Byte Position */
                        }
                }
        },
        {
                ID_OFFSET_DRIVE + M_DRIVE_BUS, /* CAN-Identifier */
                M_DRIVE_TXRX, /* Message Type */
                sizeof(float) + sizeof(float), /* DLC of Message */
                2, /* No. of Links */
                {
                        {
                                S_DRIVE_BUS_VOLTAGE,       /* Signal ID */
(                                0)|(CANFRM_LITTLE_ENDIAN)                                       /* Byte Position */
                        },
                        {
                                S_DRIVE_BUS_CURRENT,       /* Signal ID */
(                                0 + sizeof(float))|(CANFRM_LITTLE_ENDIAN)                                       /* Byte Position */
                        }
                }
        },
        {
                ID_OFFSET_DRIVE + M_DRIVE_VELOCITY, /* CAN-Identifier */
                M_DRIVE_TXRX, /* Message Type */
                sizeof(float) + sizeof(float), /* DLC of Message */
                2, /* No. of Links */
                {
                        {
                                S_DRIVE_MOTOR_VELOCITY,       /* Signal ID */
(                                0)|(CANFRM_LITTLE_ENDIAN)                                       /* Byte Position */
                        },
                        {
                                S_DRIVE_VEHICLE_VELOCITY,       /* Signal ID */
(                                0 + sizeof(float))|(CANFRM_LITTLE_ENDIAN)                                       /* Byte Position */
                        }
                }
        },
        {
                ID_OFFSET_DRIVE + M_DRIVE_PHASE_CURRENT, /* CAN-Identifier */
                M_DRIVE_TXRX, /* Message Type */
                sizeof(float) + sizeof(float), /* DLC of Message */
                2, /* No. of Links */
                {
                        {
                                S_DRIVE_PHASE_C_CURRENT,       /* Signal ID */
(                                0)|(CANFRM_LITTLE_ENDIAN)                                       /* Byte Position */
                        },
                        {
                                S_DRIVE_PHASE_B_CURRENT,       /* Signal ID */
(                                0 + sizeof(float))|(CANFRM_LITTLE_ENDIAN)                                       /* Byte Position */
                        }
                }
        },
        {
                ID_OFFSET_DRIVE + M_DRIVE_BEMF, /* CAN-Identifier */
                M_DRIVE_TXRX, /* Message Type */
                sizeof(float) + sizeof(float), /* DLC of Message */
                2, /* No. of Links */
                {
                        {
                                S_DRIVE_BEMFQ,       /* Signal ID */
(                                0)|(CANFRM_LITTLE_ENDIAN)                                       /* Byte Position */
                        },
                        {
                                S_DRIVE_BEMFD,       /* Signal ID */
(                                0 + sizeof(float))|(CANFRM_LITTLE_ENDIAN)                                       /* Byte Position */
                        }
                }
        },
        {
                ID_OFFSET_DRIVE + M_DRIVE_15V, /* CAN-Identifier */
                M_DRIVE_TXRX, /* Message Type */
                sizeof(float) + sizeof(float), /* DLC of Message */
                2, /* No. of Links */
                {
                        {
                                S_DRIVE_15V_OFFSET,       /* Signal ID */
(                                0)|(CANFRM_LITTLE_ENDIAN)                                       /* Byte Position */
                        },
                        {
                                S_DRIVE_15V,       /* Signal ID */
(                                0 + sizeof(float))|(CANFRM_LITTLE_ENDIAN)                                       /* Byte Position */
                        }
                }
        },
        {
                ID_OFFSET_DRIVE + M_DRIVE_33V_19V, /* CAN-Identifier */
                M_DRIVE_TXRX, /* Message Type */
                sizeof(float) + sizeof(float), /* DLC of Message */
                2, /* No. of Links */
                {
                        {
                                S_DRIVE_1_9V,       /* Signal ID */
(                                0)|(CANFRM_LITTLE_ENDIAN)                                       /* Byte Position */
                        },
                        {
                                S_DRIVE_3_3V,       /* Signal ID */
(                                0 + sizeof(float))|(CANFRM_LITTLE_ENDIAN)                                       /* Byte Position */
                        }
                }
        },
        {
                ID_OFFSET_DRIVE + M_DRIVE_HEATSINK_MOTOR_TEMP, /* CAN-Identifier */
                M_DRIVE_TXRX, /* Message Type */
                sizeof(float) + sizeof(float), /* DLC of Message */
                2, /* No. of Links */
                {
                        {
                                S_DRIVE_MOTOR_TEMP,       /* Signal ID */
(                                0)|(CANFRM_LITTLE_ENDIAN)                                       /* Byte Position */
                        },
                        {
                                S_DRIVE_HEATSINK_TEMP,       /* Signal ID */
(                                0 + sizeof(float))|(CANFRM_LITTLE_ENDIAN)                                       /* Byte Position */
                        }
                }
        },
        {
                ID_OFFSET_DRIVE + M_DRIVE_DSP_TEMP, /* CAN-Identifier */
                M_DRIVE_TXRX, /* Message Type */
                sizeof(float), /* DLC of Message */
                1, /* No. of Links */
                {
                        {
                                S_DRIVE_DSP_TEMP,       /* Signal ID */
(                                0)|(CANFRM_LITTLE_ENDIAN)                                       /* Byte Position */
                        }
                }
        },
        {
                ID_OFFSET_DRIVE + M_DRIVE_ODOMETER_AMPHOUR, /* CAN-Identifier */
                M_DRIVE_TXRX, /* Message Type */
                sizeof(float) + sizeof(float), /* DLC of Message */
                2, /* No. of Links */
                {
                        {
                                S_DRIVE_ODOMETER,       /* Signal ID */
(                                0)|(CANFRM_LITTLE_ENDIAN)                                       /* Byte Position */
                        },
                        {
                                S_DRIVE_DCBUS_AMPHOUR,       /* Signal ID */
(                                0 + sizeof(float))|(CANFRM_LITTLE_ENDIAN)                                       /* Byte Position */
                        }
                }
        },
/*******************************************************************/
/*      BMS      */
/********************************************************************/
        {
                ID_OFFSET_BMS + M_BMS_STATUS, /* CAN-Identifier */
                M_BMS_TXRX, /* Message Type */
                sizeof(uint16_t) + sizeof(uint32_t), /* DLC of Message */
                2, /* No. of Links */
                {
                        {
                                S_BMS_STATUS,       /* Signal ID */
                                0                                       /* Byte Position */
                        },
                        {
                                S_BMS_OSTICK,       /* Signal ID */
                                0 + sizeof(uint16_t)                                       /* Byte Position */
                        }
                }
        },
        {
                ID_OFFSET_BMS + M_BMS_CURRENT, /* CAN-Identifier */
                M_BMS_TXRX, /* Message Type */
                sizeof(int32_t), /* DLC of Message */
                1, /* No. of Links */
                {
                        {
                                S_BMS_PACK_CURRENT,       /* Signal ID */
                                0                                       /* Byte Position */
                        }
                }
        },
        {
                ID_OFFSET_BMS + M_BMS_VOLTAGE, /* CAN-Identifier */
                M_BMS_TXRX, /* Message Type */
                sizeof(uint16_t) + sizeof(uint16_t) + sizeof(uint16_t), /* DLC of Message */
                3, /* No. of Links */
                {
                        {
                                S_BMS_PACK_VOLTAGE,       /* Signal ID */
                                0                                       /* Byte Position */
                        },
                        {
                                S_BMS_SUM_VOLTAGE,       /* Signal ID */
                                0 + sizeof(uint16_t)                                       /* Byte Position */
                        },
                        {
                                S_BMS_AVERAGE_CELL_VOLTAGE,       /* Signal ID */
                                0 + sizeof(uint16_t) + sizeof(uint16_t)                                       /* Byte Position */
                        }
                }
        },
        {
                ID_OFFSET_BMS + M_BMS_CELL_VOLTAGE, /* CAN-Identifier */
                M_BMS_TXRX, /* Message Type */
                sizeof(uint16_t) + sizeof(uint8_t) + sizeof(uint16_t) + sizeof(uint8_t), /* DLC of Message */
                4, /* No. of Links */
                {
                        {
                                S_BMS_CELL_VOLTAGE_MAX,       /* Signal ID */
                                0                                       /* Byte Position */
                        },
                        {
                                S_BMS_CELL_HIGHEST_VOLTAGE,       /* Signal ID */
                                0 + sizeof(uint16_t)                                       /* Byte Position */
                        },
                        {
                                S_BMS_CELL_VOLTAGE_MIN,       /* Signal ID */
                                0 + sizeof(uint16_t) + sizeof(uint8_t)                                       /* Byte Position */
                        },
                        {
                                S_BMS_CELL_LOWEST_VOLTAGE,       /* Signal ID */
                                0 + sizeof(uint16_t) + sizeof(uint8_t) + sizeof(uint16_t)                                       /* Byte Position */
                        }
                }
        },
        {
                ID_OFFSET_BMS + M_BMS_TEMP, /* CAN-Identifier */
                M_BMS_TXRX, /* Message Type */
                sizeof(uint16_t) + sizeof(uint16_t) + sizeof(uint16_t), /* DLC of Message */
                3, /* No. of Links */
                {
                        {
                                S_BMS_HIGHEST_TEMP,       /* Signal ID */
                                0                                       /* Byte Position */
                        },
                        {
                                S_BMS_LOWEST_TEMP,       /* Signal ID */
                                0 + sizeof(uint16_t)                                       /* Byte Position */
                        },
                        {
                                S_BMS_MASTER_TEMP,       /* Signal ID */
                                0 + sizeof(uint16_t) + sizeof(uint16_t)                                       /* Byte Position */
                        }
                }
        },
        {
                ID_OFFSET_BMS + M_BMS_STATE, /* CAN-Identifier */
                M_BMS_TXRX, /* Message Type */
                sizeof(uint8_t) + sizeof(uint8_t), /* DLC of Message */
                2, /* No. of Links */
                {
                        {
                                S_BMS_IO_STATE,       /* Signal ID */
                                0                                       /* Byte Position */
                        },
                        {
                                S_BMS_SYSTEM_STATE,       /* Signal ID */
                                0 + sizeof(uint8_t)                                       /* Byte Position */
                        }
                }
        },
        {
                ID_OFFSET_BMS + M_BMS_ERRORS, /* CAN-Identifier */
                M_BMS_TXRX, /* Message Type */
                sizeof(uint32_t) + sizeof(uint32_t), /* DLC of Message */
                2, /* No. of Links */
                {
                        {
                                S_BMS_ERRORS_FLAGS,       /* Signal ID */
                                0                                       /* Byte Position */
                        },
                        {
                                S_BMS_WARNING_FLAGS,       /* Signal ID */
                                0 + sizeof(uint32_t)                                       /* Byte Position */
                        }
                }
        },
        {
                ID_OFFSET_BMS + M_BMS_CAPACITY, /* CAN-Identifier */
                M_BMS_TXRX, /* Message Type */
                sizeof(uint8_t) + sizeof(uint8_t) + sizeof(uint16_t) + sizeof(uint16_t), /* DLC of Message */
                4, /* No. of Links */
                {
                        {
                                S_BMS_SOC,       /* Signal ID */
                                0                                       /* Byte Position */
                        },
                        {
                                S_BMS_COULOMB_SOC,       /* Signal ID */
                                0 + sizeof(uint8_t)                                       /* Byte Position */
                        },
                        {
                                S_BMS_AMP_H_SUM,       /* Signal ID */
                                0 + sizeof(uint8_t) + sizeof(uint8_t)                                       /* Byte Position */
                        },
                        {
                                S_BMS_REMAINING_ENERGY,       /* Signal ID */
                                0 + sizeof(uint8_t) + sizeof(uint8_t) + sizeof(uint16_t)                                       /* Byte Position */
                        }
                }
        },
        {
                ID_OFFSET_BMS + M_BMS_DATA, /* CAN-Identifier */
                M_BMS_TXRX, /* Message Type */
                sizeof(uint32_t) + sizeof(uint32_t), /* DLC of Message */
                2, /* No. of Links */
                {
                        {
                                S_BMS_SLAVE_COMM_WARNINGS,       /* Signal ID */
                                0                                       /* Byte Position */
                        },
                        {
                                S_BMS_MASTER_POWER_UP_TIME,       /* Signal ID */
                                0 + sizeof(uint32_t)                                       /* Byte Position */
                        }
                }
        },
/*******************************************************************/
/*      DASHBOARD      */
/********************************************************************/
        {
                ID_OFFSET_DASHBOARD + M_DASHBOARD_STATUS, /* CAN-Identifier */
                M_DASHBOARD_TXRX, /* Message Type */
                sizeof(uint16_t) + sizeof(uint32_t), /* DLC of Message */
                2, /* No. of Links */
                {
                        {
                                S_DASHBOARD_STATUS,       /* Signal ID */
                                0                                       /* Byte Position */
                        },
                        {
                                S_DASHBOARD_OSTICK,       /* Signal ID */
                                0 + sizeof(uint16_t)                                       /* Byte Position */
                        }
                }
        },
        {
                ID_OFFSET_DASHBOARD + M_DASHBOARD_CTRL, /* CAN-Identifier */
                M_DASHBOARD_TXRX, /* Message Type */
                sizeof(uint8_t) + sizeof(uint8_t), /* DLC of Message */
                2, /* No. of Links */
                {
                        {
                                S_DASHBOARD_BREAK,       /* Signal ID */
                                0                                       /* Byte Position */
                        },
                        {
                                S_DASHBOARD_BUTTON,       /* Signal ID */
                                0 + sizeof(uint8_t)                                       /* Byte Position */
                        }
                }
        },
/*******************************************************************/
/*      TELEMETRIE      */
/********************************************************************/
        {
                ID_OFFSET_TELEMETRIE + M_TELEMETRIE_STATUS, /* CAN-Identifier */
                M_TELEMETRIE_TXRX, /* Message Type */
                sizeof(uint16_t) + sizeof(uint8_t) + sizeof(uint8_t) + sizeof(uint32_t), /* DLC of Message */
                4, /* No. of Links */
                {
                        {
                                S_TELEMETRIE_STATUS,       /* Signal ID */
                                0                                       /* Byte Position */
                        },
                        {
                                S_TELEMETRIE_MODEM_ON,       /* Signal ID */
                                0 + sizeof(uint16_t)                                       /* Byte Position */
                        },
                        {
                                S_TELEMETRIE_XBEE_ON,       /* Signal ID */
                                0 + sizeof(uint16_t) + sizeof(uint8_t)                                       /* Byte Position */
                        },
                        {
                                S_TELEMETRIE_OSTICK,       /* Signal ID */
                                0 + sizeof(uint16_t) + sizeof(uint8_t) + sizeof(uint8_t)                                       /* Byte Position */
                        }
                }
        },
/*******************************************************************/
/*      VOLANT      */
/********************************************************************/
        {
                ID_OFFSET_VOLANT + M_VOLANT_STATUS, /* CAN-Identifier */
                M_VOLANT_TXRX, /* Message Type */
                sizeof(uint16_t) + sizeof(uint32_t), /* DLC of Message */
                2, /* No. of Links */
                {
                        {
                                S_VOLANT_STATUS,       /* Signal ID */
                                0                                       /* Byte Position */
                        },
                        {
                                S_VOLANT_OSTICK,       /* Signal ID */
                                0 + sizeof(uint16_t)                                       /* Byte Position */
                        }
                }
        },
        {
                ID_OFFSET_VOLANT + M_VOLANT_CTRL, /* CAN-Identifier */
                M_VOLANT_TXRX, /* Message Type */
                sizeof(uint8_t) + sizeof(uint16_t), /* DLC of Message */
                2, /* No. of Links */
                {
                        {
                                S_VOLANT_OPMODE,       /* Signal ID */
                                0                                       /* Byte Position */
                        },
                        {
                                S_VOLANT_BUTTON,       /* Signal ID */
                                0 + sizeof(uint8_t)                                       /* Byte Position */
                        }
                }
        },
/*******************************************************************/
/*      POWERSUPPLY      */
/********************************************************************/
        {
                ID_OFFSET_POWERSUPPLY + M_POWERSUPPLY_STATUS, /* CAN-Identifier */
                M_POWERSUPPLY_TXRX, /* Message Type */
                sizeof(uint16_t) + sizeof(uint32_t), /* DLC of Message */
                2, /* No. of Links */
                {
                        {
                                S_POWERSUPPLY_STATUS,       /* Signal ID */
                                0                                       /* Byte Position */
                        },
                        {
                                S_POWERSUPPLY_OSTICK,       /* Signal ID */
                                0 + sizeof(uint16_t)                                       /* Byte Position */
                        }
                }
        },
        {
                ID_OFFSET_POWERSUPPLY + M_POWERSUPPLY_CAN, /* CAN-Identifier */
                M_POWERSUPPLY_TXRX, /* Message Type */
                sizeof(int16_t) + sizeof(int16_t), /* DLC of Message */
                2, /* No. of Links */
                {
                        {
                                S_POWERSUPPLY_12V_CAN_COURANT,       /* Signal ID */
                                0                                       /* Byte Position */
                        },
                        {
                                S_POWERSUPPLY_12V_CAN_VOLTAGE,       /* Signal ID */
                                0 + sizeof(int16_t)                                       /* Byte Position */
                        }
                }
        },
        {
                ID_OFFSET_POWERSUPPLY + M_POWERSUPPLY_HP, /* CAN-Identifier */
                M_POWERSUPPLY_TXRX, /* Message Type */
                sizeof(int16_t) + sizeof(int16_t), /* DLC of Message */
                2, /* No. of Links */
                {
                        {
                                S_POWERSUPPLY_12V_HP_COURANT,       /* Signal ID */
                                0                                       /* Byte Position */
                        },
                        {
                                S_POWERSUPPLY_12V_HP_VOLTAGE,       /* Signal ID */
                                0 + sizeof(int16_t)                                       /* Byte Position */
                        }
                }
        },
        {
                ID_OFFSET_POWERSUPPLY + M_POWERSUPPLY_AUX, /* CAN-Identifier */
                M_POWERSUPPLY_TXRX, /* Message Type */
                sizeof(int16_t) + sizeof(int16_t), /* DLC of Message */
                2, /* No. of Links */
                {
                        {
                                S_POWERSUPPLY_12V_AUX_COURANT,       /* Signal ID */
                                0                                       /* Byte Position */
                        },
                        {
                                S_POWERSUPPLY_12V_AUX_VOLTAGE,       /* Signal ID */
                                0 + sizeof(int16_t)                                       /* Byte Position */
                        }
                }
        },
/*******************************************************************/
/*      IGNITION      */
/********************************************************************/
        {
                ID_OFFSET_IGNITION + M_IGNITION_ID, /* CAN-Identifier */
                M_IGNITION_TXRX, /* Message Type */
                sizeof(uint8_t), /* DLC of Message */
                1, /* No. of Links */
                {
                        {
                                S_IGNITION_STATUS1,       /* Signal ID */
                                0                                       /* Byte Position */
                        }
                }
        },
/*******************************************************************/
/*      FLASHER      */
/********************************************************************/
        {
                ID_OFFSET_FLASHER + M_FLASHER_TOP, /* CAN-Identifier */
                M_FLASHER_TXRX, /* Message Type */
                sizeof(uint16_t) + sizeof(uint32_t), /* DLC of Message */
                2, /* No. of Links */
                {
                        {
                                S_FLASHER_1_STATUS,       /* Signal ID */
                                0                                       /* Byte Position */
                        },
                        {
                                S_FLASHER_1_OSTICK,       /* Signal ID */
                                0 + sizeof(uint16_t)                                       /* Byte Position */
                        }
                }
        },
        {
                ID_OFFSET_FLASHER + M_FLASHER_BOT, /* CAN-Identifier */
                M_FLASHER_TXRX, /* Message Type */
                sizeof(uint16_t) + sizeof(uint32_t), /* DLC of Message */
                2, /* No. of Links */
                {
                        {
                                S_FLASHER_2_STATUS,       /* Signal ID */
                                0                                       /* Byte Position */
                        },
                        {
                                S_FLASHER_2_OSTICK,       /* Signal ID */
                                0 + sizeof(uint16_t)                                       /* Byte Position */
                        }
                }
        },
/*******************************************************************/
/*      MUPPET      */
/********************************************************************/
        {
                ID_OFFSET_MUPPET + M_MUPPET_STATUS_MPPT1, /* CAN-Identifier */
                M_MUPPET_TXRX, /* Message Type */
                sizeof(uint8_t) + sizeof(uint8_t), /* DLC of Message */
                2, /* No. of Links */
                {
                        {
                                S_MUPPET_FLAG_MPPT1,       /* Signal ID */
                                0                                       /* Byte Position */
                        },
                        {
                                S_MUPPET_TEMP_MPPT1,       /* Signal ID */
                                0 + sizeof(uint8_t)                                       /* Byte Position */
                        }
                }
        },
        {
                ID_OFFSET_MUPPET + M_MUPPET_I_MPPT1, /* CAN-Identifier */
                M_MUPPET_TXRX, /* Message Type */
                sizeof(float) + sizeof(float), /* DLC of Message */
                2, /* No. of Links */
                {
                        {
                                S_MUPPET_IIN_MPPT1,       /* Signal ID */
                                0                                       /* Byte Position */
                        },
                        {
                                S_MUPPET_IOUT_MPPT1,       /* Signal ID */
                                0 + sizeof(float)                                       /* Byte Position */
                        }
                }
        },
        {
                ID_OFFSET_MUPPET + M_MUPPET_U_MPPT1, /* CAN-Identifier */
                M_MUPPET_TXRX, /* Message Type */
                sizeof(float) + sizeof(float), /* DLC of Message */
                2, /* No. of Links */
                {
                        {
                                S_MUPPET_UIN_MPPT1,       /* Signal ID */
                                0                                       /* Byte Position */
                        },
                        {
                                S_MUPPET_UOUT_MPPT1,       /* Signal ID */
                                0 + sizeof(float)                                       /* Byte Position */
                        }
                }
        },
        {
                ID_OFFSET_MUPPET + M_MUPPET_STATUS_MPPT2, /* CAN-Identifier */
                M_MUPPET_TXRX, /* Message Type */
                sizeof(uint8_t) + sizeof(uint8_t), /* DLC of Message */
                2, /* No. of Links */
                {
                        {
                                S_MUPPET_FLAG_MPPT2,       /* Signal ID */
                                0                                       /* Byte Position */
                        },
                        {
                                S_MUPPET_TEMP_MPPT2,       /* Signal ID */
                                0 + sizeof(uint8_t)                                       /* Byte Position */
                        }
                }
        },
        {
                ID_OFFSET_MUPPET + M_MUPPET_I_MPPT2, /* CAN-Identifier */
                M_MUPPET_TXRX, /* Message Type */
                sizeof(float) + sizeof(float), /* DLC of Message */
                2, /* No. of Links */
                {
                        {
                                S_MUPPET_IIN_MPPT2,       /* Signal ID */
                                0                                       /* Byte Position */
                        },
                        {
                                S_MUPPET_IOUT_MPPT2,       /* Signal ID */
                                0 + sizeof(float)                                       /* Byte Position */
                        }
                }
        },
        {
                ID_OFFSET_MUPPET + M_MUPPET_U_MPPT2, /* CAN-Identifier */
                M_MUPPET_TXRX, /* Message Type */
                sizeof(float) + sizeof(float), /* DLC of Message */
                2, /* No. of Links */
                {
                        {
                                S_MUPPET_UIN_MPPT2,       /* Signal ID */
                                0                                       /* Byte Position */
                        },
                        {
                                S_MUPPET_UOUT_MPPT2,       /* Signal ID */
                                0 + sizeof(float)                                       /* Byte Position */
                        }
                }
        },
        {
                ID_OFFSET_MUPPET + M_MUPPET_STATUS_MPPT3, /* CAN-Identifier */
                M_MUPPET_TXRX, /* Message Type */
                sizeof(uint8_t) + sizeof(uint8_t), /* DLC of Message */
                2, /* No. of Links */
                {
                        {
                                S_MUPPET_FLAG_MPPT3,       /* Signal ID */
                                0                                       /* Byte Position */
                        },
                        {
                                S_MUPPET_TEMP_MPPT3,       /* Signal ID */
                                0 + sizeof(uint8_t)                                       /* Byte Position */
                        }
                }
        },
        {
                ID_OFFSET_MUPPET + M_MUPPET_I_MPPT3, /* CAN-Identifier */
                M_MUPPET_TXRX, /* Message Type */
                sizeof(float) + sizeof(float), /* DLC of Message */
                2, /* No. of Links */
                {
                        {
                                S_MUPPET_IIN_MPPT3,       /* Signal ID */
                                0                                       /* Byte Position */
                        },
                        {
                                S_MUPPET_IOUT_MPPT3,       /* Signal ID */
                                0 + sizeof(float)                                       /* Byte Position */
                        }
                }
        },
        {
                ID_OFFSET_MUPPET + M_MUPPET_U_MPPT3, /* CAN-Identifier */
                M_MUPPET_TXRX, /* Message Type */
                sizeof(float) + sizeof(float), /* DLC of Message */
                2, /* No. of Links */
                {
                        {
                                S_MUPPET_UIN_MPPT3,       /* Signal ID */
                                0                                       /* Byte Position */
                        },
                        {
                                S_MUPPET_UOUT_MPPT3,       /* Signal ID */
                                0 + sizeof(float)                                       /* Byte Position */
                        }
                }
        },
        {
                ID_OFFSET_MUPPET + M_MUPPET_STATUS_MPPT4, /* CAN-Identifier */
                M_MUPPET_TXRX, /* Message Type */
                sizeof(uint8_t) + sizeof(uint8_t), /* DLC of Message */
                2, /* No. of Links */
                {
                        {
                                S_MUPPET_FLAG_MPPT4,       /* Signal ID */
                                0                                       /* Byte Position */
                        },
                        {
                                S_MUPPET_TEMP_MPPT4,       /* Signal ID */
                                0 + sizeof(uint8_t)                                       /* Byte Position */
                        }
                }
        },
        {
                ID_OFFSET_MUPPET + M_MUPPET_I_MPPT4, /* CAN-Identifier */
                M_MUPPET_TXRX, /* Message Type */
                sizeof(float) + sizeof(float), /* DLC of Message */
                2, /* No. of Links */
                {
                        {
                                S_MUPPET_IIN_MPPT4,       /* Signal ID */
                                0                                       /* Byte Position */
                        },
                        {
                                S_MUPPET_IOUT_MPPT4,       /* Signal ID */
                                0 + sizeof(float)                                       /* Byte Position */
                        }
                }
        },
        {
                ID_OFFSET_MUPPET + M_MUPPET_U_MPPT4, /* CAN-Identifier */
                M_MUPPET_TXRX, /* Message Type */
                sizeof(float) + sizeof(float), /* DLC of Message */
                2, /* No. of Links */
                {
                        {
                                S_MUPPET_UIN_MPPT4,       /* Signal ID */
                                0                                       /* Byte Position */
                        },
                        {
                                S_MUPPET_UOUT_MPPT4,       /* Signal ID */
                                0 + sizeof(float)                                       /* Byte Position */
                        }
                }
        },
/*******************************************************************/
/*      TEMPLATE      */
/********************************************************************/
        {
                ID_OFFSET_TEMPLATE + TEMPLATE_STATUS, /* CAN-Identifier */
                M_TEMPLATE_TXRX, /* Message Type */
                sizeof(uint16_t) + sizeof(uint32_t) + sizeof(uint8_t), /* DLC of Message */
                3, /* No. of Links */
                {
                        {
                                S_TEMPLATE_STATUS,       /* Signal ID */
                                0                                       /* Byte Position */
                        },
                        {
                                S_TEMPLATE_OSTICK,       /* Signal ID */
                                0 + sizeof(uint16_t)                                       /* Byte Position */
                        },
                        {
                                S_TEMPLATE_LED,       /* Signal ID */
                                0 + sizeof(uint16_t) + sizeof(uint32_t)                                       /* Byte Position */
                        }
                }
        },
#ifdef E92_USE_CUSTOM_MEMSTRUCT
/*******************************************************************/
/*                                                    CUSTOM CAN                                                         */
/********************************************************************/
        CUSTOM_CAN_MSG,
#endif
        /*******************************************************************/
        /*                                                        Last Item                                                                        */
        /********************************************************************/
        {
                0, /* CAN-Identifier */
                0, /* Message Type */
                0, /* DLC of Message */
                0, /* No. of Links */
        },
};

#endif /*EXCLUDE_MAIN_MEMSTRUCT*/
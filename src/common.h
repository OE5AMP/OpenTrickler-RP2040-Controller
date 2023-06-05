#ifndef COMMON_H_
#define COMMON_H_

#include <stdint.h>
#include <FreeRTOS.h>


#ifdef __cplusplus
extern "C" {
#endif


/**
 * If the RTOS is running then use RTOS delay. Otherwise use dummy delay. 
*/
void delay_ms(uint32_t ms, BaseType_t scheduler_state);

const char * boolean_string(bool var);


#ifdef __cplusplus
}
#endif


#endif // COMMON_H_
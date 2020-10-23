#include <linux/build-salt.h>
#include <linux/module.h>
#include <linux/vermagic.h>
#include <linux/compiler.h>

BUILD_SALT;

MODULE_INFO(vermagic, VERMAGIC_STRING);
MODULE_INFO(name, KBUILD_MODNAME);

__visible struct module __this_module
__section(.gnu.linkonce.this_module) = {
	.name = KBUILD_MODNAME,
	.init = init_module,
#ifdef CONFIG_MODULE_UNLOAD
	.exit = cleanup_module,
#endif
	.arch = MODULE_ARCH_INIT,
};

#ifdef CONFIG_RETPOLINE
MODULE_INFO(retpoline, "Y");
#endif

static const struct modversion_info ____versions[]
__used __section(__versions) = {
	{ 0x93a58f87, "module_layout" },
	{ 0x8ad9de86, "param_ops_uint" },
	{ 0xfe990052, "gpio_free" },
	{ 0xff938571, "gpiod_unexport" },
	{ 0xae96f8ed, "kthread_stop" },
	{ 0x7c07594b, "wake_up_process" },
	{ 0x82b71136, "kthread_create_on_node" },
	{ 0xe21b246f, "gpiod_export" },
	{ 0x10ecc63, "gpiod_direction_output_raw" },
	{ 0x47229b5c, "gpio_request" },
	{ 0xedbfbd3f, "kobject_put" },
	{ 0x8b3faaa4, "sysfs_create_group" },
	{ 0x14798c46, "kobject_create_and_add" },
	{ 0x55abedfc, "kernel_kobj" },
	{ 0xbcab6ee6, "sscanf" },
	{ 0x84b183ae, "strncmp" },
	{ 0xdecd0b29, "__stack_chk_fail" },
	{ 0xf9a482f9, "msleep" },
	{ 0xa6520880, "gpiod_set_raw_value" },
	{ 0x406fd5fc, "gpio_to_desc" },
	{ 0xb3f7646e, "kthread_should_stop" },
	{ 0xc5850110, "printk" },
	{ 0x8f678b07, "__stack_chk_guard" },
	{ 0x3c3ff9fd, "sprintf" },
	{ 0xb1ad28e0, "__gnu_mcount_nc" },
};

MODULE_INFO(depends, "");


MODULE_INFO(srcversion, "14EE5DD6B814E5193907BD8");

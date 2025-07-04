rule = {
  matches = {
    {{"device.name", "equals", "alsa_input.usb-HD_Web_Camera_HD_Web_Camera_Ucamera001-02.5"}},
  },
  apply_properties = {
    ["device.disabled"] = true,
  }
}
table.insert(alsa_monitor.rules,rule)

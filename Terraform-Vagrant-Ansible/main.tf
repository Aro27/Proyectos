resource "null_resource" "ubuntu_vagrant" {
  provisioner "local-exec" {
    command = "vagrant up"
  }
}

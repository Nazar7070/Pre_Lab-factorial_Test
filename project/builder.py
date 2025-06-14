class Computer:
    def __init__(self):
        self.parts = []

    def add(self, part):
        self.parts.append(part)

    def list_parts(self):
        return self.parts


class ComputerBuilder:
    def reset(self):
        self.computer = Computer()

    def add_cpu(self): pass
    def add_gpu(self): pass
    def add_ram(self): pass
    def get_result(self): return self.computer


class OfficePCBuilder(ComputerBuilder):
    def __init__(self): self.reset()
    def add_cpu(self): self.computer.add("Intel i3")
    def add_gpu(self): self.computer.add("Integrated GPU")
    def add_ram(self): self.computer.add("8GB RAM")


class GamingPCBuilder(ComputerBuilder):
    def __init__(self): self.reset()
    def add_cpu(self): self.computer.add("Intel i9")
    def add_gpu(self): self.computer.add("NVIDIA RTX 4080")
    def add_ram(self): self.computer.add("32GB RAM")


class ServerPCBuilder(ComputerBuilder):
    def __init__(self): self.reset()
    def add_cpu(self): self.computer.add("AMD EPYC")
    def add_gpu(self): self.computer.add("None")
    def add_ram(self): self.computer.add("64GB ECC RAM")

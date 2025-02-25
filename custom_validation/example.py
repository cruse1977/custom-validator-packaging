from extras.validators import CustomValidator

class MyValidator(CustomValidator):

    def validate(self, instance, request):
        if instance.status == 'active' and not instance.description:
            self.fail("Active sites must have a description set!", field='status')
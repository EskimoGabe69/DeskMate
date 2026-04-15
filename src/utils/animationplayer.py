class Animation:
    def __init__(self, frames, frame_duration) -> None:
        self.frames = frames
        self.frame_duration = frame_duration
        self.animation_duration = len(self.frames)*self.frame_duration

    def get_frame(self, state_time):
        if len(self.frames) == 1:
            return self.frames[0]

        frame_number = int(state_time/self.frame_duration)

        frame_number = min(len(self.frames) - 1, frame_number)

        return self.frames[frame_number]

    def is_animation_finished(self, state_time):
        frame_number = int(state_time  / self.frame_duration)
        return len(self.frames) - 1 < frame_number

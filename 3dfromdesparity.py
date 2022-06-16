def stereo_match(imgL, imgR):
    # disparity range is tuned for 'aloe' image pair
    window_size = 15
    min_disp = 16
    num_disp = 96 - min_disp
    stereo = cv2.StereoSGBM_create(minDisparity=min_disp,
                                   numDisparities=num_disp,
                                   blockSize=16,
                                   P1=8 * 3 * window_size ** 2,
                                   P2=32 * 3 * window_size ** 2,
                                   disp12MaxDiff=1,
                                   uniquenessRatio=10,
                                   speckleWindowSize=150,
                                   speckleRange=32
                                   )

    # print('computing disparity...')
    disp = stereo.compute(imgL, imgR).astype(np.float32) / 16.0

    # print('generating 3d point cloud...',)
    h, w = imgL.shape[:2]
    f = 0.8 * w  # guess for focal length
    Q = np.float32([[1, 0, 0, -0.5 * w],
                    [0, -1, 0, 0.5 * h],  # turn points 180 deg around x-axis,
                    [0, 0, 0, -f],  # so that y-axis looks up
                    [0, 0, 1, 0]])
    points = cv2.reprojectImageTo3D(disp, Q)
    colors = cv2.cvtColor(imgL, cv2.COLOR_BGR2RGB)
    mask = disp > disp.min()
    out_points = points[mask]
    out_colors = colors[mask]
    append_ply_array(out_points, out_colors)

    disparity_scaled = (disp - min_disp) / num_disp
    disparity_scaled += abs(np.amin(disparity_scaled))
    disparity_scaled /= np.amax(disparity_scaled)
    disparity_scaled[disparity_scaled < 0] = 0
    return np.array(255 * disparity_scaled, np.uint8) 





def get_3d(cls, disparity, disparity_to_depth_map):
        """Compute point cloud."""
        return cv2.reprojectImageTo3D(disparity, disparity_to_depth_map) 







def get3DImageFromDisparity(self, disparity, Q):
        """
        **SUMMARY**

        This method returns the 3D depth image using reprojectImageTo3D method.

        **PARAMETERS**
        * *disparity* - Disparity Image
        * *Q* - reprojection Matrix (disparity to depth matrix)

        **RETURNS**

        SimpleCV.Image representing 3D depth Image
        also StereoCamera.Image3D gives OpenCV 3D Depth Image of CV_32F type.

        **EXAMPLE**

        >>> lImage = Image("l.jpg")
        >>> rImage = Image("r.jpg")
        >>> stereo = StereoCamera()
        >>> Q = cv.Load("Q.yml")
        >>> disp = stereo.findDisparityMap()
        >>> stereo.get3DImageFromDisparity(disp, Q)
        """
        cv2flag = True
        try:
            import cv2
        except ImportError:
            cv2flag = False
            import cv2.cv as cv

        if cv2flag:
            if not isinstance(Q, np.ndarray):
                Q = np.array(Q)
            disparity = disparity.getNumpyCv2()    
            Image3D = cv2.reprojectImageTo3D(disparity, Q, ddepth=cv2.cv.CV_32F)
            Image3D_normalize = cv2.normalize(Image3D, alpha=0, beta=255, norm_type=cv2.cv.CV_MINMAX, dtype=cv2.cv.CV_8UC3)
            retVal = Image(Image3D_normalize, cv2image=True)
        else:
            disparity = disparity.getMatrix()
            Image3D = cv.CreateMat(self.LeftImage.size()[1], self.LeftImage.size()[0], cv2.cv.CV_32FC3)
            Image3D_normalize = cv.CreateMat(self.LeftImage.size()[1], self.LeftImage.size()[0], cv2.cv.CV_8UC3)
            cv.ReprojectImageTo3D(disparity, Image3D, Q)
            cv.Normalize(Image3D, Image3D_normalize, 0, 255, cv.CV_MINMAX, CV_8UC3)
            retVal = Image(Image3D_normalize)
        self.Image3D = Image3D
        return retVal 
